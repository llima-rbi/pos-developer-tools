import React, { Component } from 'react'
import './dashboard.css'

class Dashboard extends Component {
    render() {
        return (
            <div className={`dashboard dashboard__${this.props.position}`}>
                {this.props.children}
            </div>
        )
    }
}

export default Dashboard