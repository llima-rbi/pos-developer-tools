import React, { Component } from 'react'
import { Route, Redirect } from 'react-router-dom'

class PrivateRoute extends Component {
  render() {
    const Component = this.props.component
    const token = localStorage.getItem('TOKEN')

    if (token) {
      return (<Route render={ () => <Component {...this.props} /> } />)
    } else {
      return (<Redirect to="/login" />)
    }
  }
}

export default PrivateRoute