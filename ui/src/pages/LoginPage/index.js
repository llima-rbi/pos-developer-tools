import React, { Component, Fragment, createRef } from 'react'
import Header from '../../components/Header'

import './loginPage.css'
import Widget from '../../components/Widget'

class LoginPage extends Component {
  constructor(props) {
    super(props)
    this.state = {
      loginError: false
    }

    this.username = createRef()
    this.password = createRef()
  }

  handleLogin = (event) => {
    event.preventDefault()

    const loginRequest = {
      username: this.username.current.value,
      password: this.password.current.value
    }

    fetch('http://localhost:8181/api/login', {
      method: 'POST',
      body: JSON.stringify(loginRequest)
    }).then((response) => {
        if (response.ok) {
          return response
        }
        else {
          this.setState({loginError: true})
        }
      }
    ).then((loginResponse) => {
      if (loginResponse) {
        localStorage.setItem('TOKEN', loginResponse)
        this.props.history.push('/')
      }
    })
      .catch((error) => {
        console.error(error)
        this.setState({loginError: true})
      }
    )
  }

  render() {
    const {
      loginError
    } = this.state

    return (
      <Fragment>
        <Header />
        <div className="loginPage">
          <div className="container">
            <Widget>
              <h2 className="loginPage__title">Seja bem vindo!</h2>
              <form className="loginPage__form" action="/">
                <div className="loginPage__inputWrap">
                  <label className="loginPage__label" htmlFor="username">Login</label>
                  <input ref={this.username} className="loginPage__input" type="text" id="username" name="username" />
                </div>
                <div className="loginPage__inputWrap">
                  <label className="loginPage__label" htmlFor="password">Senha</label>
                  <input ref={this.password} className="loginPage__input" type="password" id="password" name="password" />
                </div>
                {(loginError &&
                  <div className="loginPage__errorBox">
                    Erro autenticando usuário!
                  </div>)}
                <div className="loginPage__inputWrap">
                  <button onClick={this.handleLogin} className="loginPage__btnLogin" type="submit">
                    Logar
                  </button>
                </div>
              </form>
            </Widget>
          </div>
        </div>
      </Fragment>
    )
  }
}


export default LoginPage