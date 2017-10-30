import React, { Component } from 'react';
import { Switch, Route } from 'react-router-dom';
import './App.css';

import Intro from './Intro';
import Table from './Table';

class App extends Component {
  constructor() {
    super();
    this.state = {

    }
  }

  render() {
    return (

        <div className="App">

          <header className="App-header">
            <h1 className="App-title">Petition</h1>
          </header>

          <Switch>
            <Route exact path='/' component={Intro}/>
            <Route path='/petition/:id' component={Table}/>
          </Switch>
        </div>
    );
  }
}

export default App;
