import React, { Component } from 'react'
import Dashboard from '../../components/Dashboard'

class RemoteHvScreen extends Component {
  constructor(props) {
    super(props)
    this.state = {}
  }

  render() {
    return (
      <div className="container">
        <Dashboard position="centro">
          <dev>Teste</dev>
        </Dashboard>
      </div>
    );
  }
}

export default RemoteHvScreen;
