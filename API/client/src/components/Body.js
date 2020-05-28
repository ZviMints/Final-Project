import React, { Component } from 'react';

import Visualization from './Visualization'
import Abstract from './Abstract'
import About from './About'
import Process from './Process'
import Button from 'react-bootstrap/Button'

class Body extends Component {
  constructor(props) {
    super(props);
    this.state = {
      pageName: "visualization",
      page: <Visualization/>
    };
  }

   handleClick = (name,value) => {
      this.setState({ pageName: name, page: value })
  }

  render() {
    return (
      <div>
        <div id="menu">
          <Button className="button" variant={this.state.pageName === "visualization" ? "success" : "light"} onClick={() => this.handleClick("visualization",<Visualization />)}>Visualization</Button>
          <Button className="button" variant={this.state.pageName === "abstract" ? "success" : "light"} onClick={() => this.handleClick("abstract",<Abstract />)}>Abstract</Button>
          <Button className="button" variant={this.state.pageName === "about" ? "success" : "light"} onClick={() => this.handleClick("about",<About />)}>About Us</Button>
          <Button className="button" variant={this.state.pageName === "process" ? "success" : "light"} onClick={() => this.handleClick("process",<Process />)}>Our Process</Button>
        </div>
        <div id="body">
          {this.state.page}
        </div>
      </div>
    );
  }
}

export default Body;
