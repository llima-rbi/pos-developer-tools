from functools import wraps

from application.model import InternalError
from application.service import LoginService
from flask import request, Response, jsonify
from typing import List, Optional

server_allowed_urls = {}
login_service = None  # type: Optional[LoginService]


def set_allowed_urls(allowed_urls):
    # type: (List[str]) -> None
    
    global server_allowed_urls
    
    for allowed_url in allowed_urls:
        server_allowed_urls[allowed_url] = allowed_url


def default_header(f):
    @wraps(f)
    def decorated_function(*args, **kargs):
        response = f(*args, **kargs)
        
        if response is None:
            response = Response()
        
        if isinstance(response, str):
            response = Response(response)
            response.headers["Content-Type"] = "application/json"
        
        if isinstance(response, tuple):
            if isinstance(response[0], str):
                response = Response(response[0], response[1])
                response.headers["Content-Type"] = "application/json"
            elif isinstance(response[0], Response):
                original_tuple = response
                
                response = response[0]
                if len(original_tuple) > 1:
                    response.status = str(original_tuple[1])
        
        if "Origin" in request.headers:
            origin = request.headers["Origin"]
            if origin is not None \
                    and origin in server_allowed_urls \
                    and "Access-Control-Allow-Origin" not in response.headers:
                response.headers.add("Access-Control-Allow-Origin", origin)
        
        return response
    return decorated_function


def has_auth_token(f):
    @wraps(f)
    def decorated_function(*args, **kargs):
        try:
            if "Auth-Token" not in request.headers:
                return "", 401

            auth_token = request.headers.get('Auth-Token')
            if not auth_token:
                return "", 401

            if not login_service.is_valid_token(auth_token):
                return "", 401
            
        except Exception as ex:
            error_object = InternalError(repr(ex))
            return jsonify(error_object), 500

        return f(*args, **kargs)

    return decorated_function
