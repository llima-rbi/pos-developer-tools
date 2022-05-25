import React, { Component } from 'react'
import './header.css'

class Header extends Component {
    render() {
        return (
            <header className="header">
                <div className="header__container container">
                    <h1 className="header__logo">
                        <a href="/">Pos Developer Tools</a>
                    </h1>
                    { this.props.children }
                </div>
            </header>
        )
    }
}

export default Header