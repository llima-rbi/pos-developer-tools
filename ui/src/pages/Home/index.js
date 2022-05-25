import React, { Component, Fragment } from 'react'
import FunctionButton from '../../components/FunctionButton/FunctionButton'
import NavMenu from '../../components/NavMenu'
import Header from '../../components/Header'
import RemoteHvScreen from '../RemoteHV'
import Dashboard from '../../components/Dashboard'

const styles = {
  container: {
    display: 'flex',
    width: '100%',
    height: '100%',
    position: 'absolute'
  },
  buttonsGroup: {
    flexGrow: 1,
    flexShrink: 0,
    flexBasis: 0,
    position: 'relative',
    margin: '0.5vw',
    background: 'rgb(255, 255, 255)'
  },
  gridPadding: {
    padding: '1px'
  },
  disabledBtn: {
    backgroundColor: '#8e8f91',
    color: '#000000'
  },
  darkBtn: {
    backgroundColor: '#3f3d3d',
    color: '#ffffff'
  }
}

class Home extends Component {
  constructor(props) {
    super(props)
    this.state = {
      selectedScreenName: null,
      selectedScreen: null
    }
  }

  selectionScreen = () => {
    return (
      <div style={styles.container}>
        <div style={styles.buttonsGroup}>
          <FunctionButton
            name={'RemoteHV'}
            setScreenFunc={this.setSelectScreen}
            classes={styles.darkBtn}
          />
        </div>
      </div>
    )
  }

  setSelectScreen = (screenName) => {
    if (screenName === 'RemoteHV') {
      this.setState({ selectedScreenName: screenName, selectedScreen: <RemoteHvScreen/> })
    }
  }


  render() {
    const { selectedScreenName, selectedScreen } = this.state

    let renderedScreen
    if (selectedScreenName != null) {
      renderedScreen = selectedScreen
    } else {
      renderedScreen = this.selectionScreen()
    }

    return (
      <Fragment>
        <Header>
          <NavMenu user="@admin"/>
        </Header>
        <div className="container">
          <Dashboard position="centro">
            {renderedScreen}
          </Dashboard>
        </div>
      </Fragment>
    );
  }
}

export default Home
