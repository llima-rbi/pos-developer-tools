import json
from logging import Logger
from threading import Thread

import requests
from application.model import InternalError, BadRequest, AuthorizationFailed
from application.server import default_header, has_auth_token
from application.service import LoginService, StoresService
from flask import Flask, request, jsonify
from typing import Optional

app = Flask("FlaskRoutes")
logger = None  # type: Optional[Logger]
login_service = None  # type: Optional[LoginService]
stores_service = None  # type: Optional[StoresService]


class FlaskServer(object):
    def __init__(self, logger, port, login_service, stores_service):
        # type: (Logger, int, LoginService, StoresService) -> None
        
        self.app_thread = None
        self.port = port
        
        self.logger = logger
        self.login_service = login_service
        self.stores_service = stores_service

    def start(self):
        self.app_thread = Thread(target=app.run, kwargs={"port": self.port, "host": "0.0.0.0", "threaded": True})
        self.app_thread.daemon = True
        self.app_thread.start()

    def stop(self):
        if self.app_thread is None:
            return

        requests.request("POST", "http://localhost:{0}".format(self.port) + "/api/shutdown")
        
    def configure_globals(self):
        global logger
        global login_service
        global stores_service
        
        logger = self.logger
        login_service = self.login_service
        stores_service = self.stores_service


@app.route('/api/login', methods=['POST'])
@default_header
def login():
    try:
        data = json.loads(request.data)
        
        user_name = data.get("username")
        if not user_name:
            return jsonify(BadRequest("user", "user is empty", "user is empty")), 400
        
        password = data.get("username")
        if not password:
            return jsonify(BadRequest("password", "password is empty", "password is empty")), 400

        auth_token = login_service.login(user_name, password)
        return auth_token, 200
    except AuthorizationFailed:
        return "", 403
    except Exception as ex:
        logger.exception("Login error")
        error_object = InternalError(repr(ex))
        return jsonify(error_object), 500
    
    
@app.route('/api/logout', methods=['POST'])
@default_header
@has_auth_token
def logout():
    try:
        auth_token = request.headers.get('Auth-Token')
        login_service.logout(auth_token)
        return "", 200
    except Exception as ex:
        logger.exception("Logout error")
        error_object = InternalError(repr(ex))
        return jsonify(error_object), 500


@app.route("/api/getAllStores", methods=['GET'])
@default_header
def get_tasks():
    try:
        return stores_service.get_all_stores()
    except Exception as ex:
        logger.exception("Login error")
        error_object = InternalError(repr(ex))
        return jsonify(error_object), 500


@app.route("/api/shutdown", methods=['POST'])
def shutdown():
    func = request.environ.get("werkzeug.server.shutdown")
    if func is None:
        raise RuntimeError("Not running with the Werkzeug Server")
    func()
    return "Server shutting down..."
