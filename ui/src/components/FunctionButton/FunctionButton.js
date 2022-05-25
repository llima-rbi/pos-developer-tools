import React, { Component } from 'react'
import PropTypes from 'prop-types'

export default class FunctionButton extends Component {

  render() {
    const { name, key, classes, disabled, setScreenFunc } = this.props

    return (
      <button
        key={key}
        disabled={disabled}
        onClick={() => setScreenFunc(name)}
      >
        {name}
      </button>
    )
  }
}

FunctionButton.propTypes = {
  name: PropTypes.string,
  key: PropTypes.string,
  classes: PropTypes.object,
  disabled: PropTypes.bool,
  setScreenFunc: PropTypes.func
}
