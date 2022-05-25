import React, { Component } from 'react'
import { BrowserRouter, Switch, Route } from 'react-router-dom'
import Home from './pages/Home'
import Login from './pages/LoginPage'
import PrivateRoute from './components/PrivateRoute'

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <Switch>
          <PrivateRoute path="/" component={Home} exact />
          <Route path="/login" component={Login} />
        </Switch>
      </BrowserRouter>
    )
  }
}

export default App
