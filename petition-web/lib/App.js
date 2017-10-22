import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import './table';

class App extends Component {
  constructor() {
    super();
    this.state = {};
  }

  render() {
    return React.createElement(
      'div',
      { className: 'App' },
      React.createElement(
        'header',
        { className: 'App-header' },
        React.createElement('img', { src: logo, className: 'App-logo', alt: 'logo' }),
        React.createElement(
          'h1',
          { className: 'App-title' },
          'Welcome to React'
        )
      ),
      React.createElement(
        'p',
        { className: 'App-intro' },
        'To get started, edit ',
        React.createElement(
          'code',
          null,
          'src/App.js'
        ),
        ' and save to reload.'
      ),
      React.createElement('table', null)
    );
  }
}

export default App;