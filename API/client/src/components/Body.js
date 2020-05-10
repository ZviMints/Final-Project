import React, { Component } from 'react';

import Visualization from './Visualization'
import Abstract from './Abstract'
import About from './About'
import Process from './Process'

class Body extends Component {
  constructor(props) {
    super(props);
    this.state = {
      "page": <Visualization />,
    };
  }

   handleClick = (component) => {
    this.setState({page : component})
  }

  render() {
    return (
      <div>
        <div id="menu">
          <button onClick={() => this.handleClick(<Visualization />)}>Visualization</button>
          <button onClick={() => this.handleClick(<Abstract />)}>Abstract</button>
          <button onClick={() => this.handleClick(<About />)}>About Us</button>
          <button onClick={() => this.handleClick(<Process />)}>Our Process</button>
        </div>
        <div id="body">
          {this.state.page}
        </div>
      </div>
    );
  }
}

export default Body;
