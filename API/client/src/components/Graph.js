import React, { Component } from 'react';

class Graph extends Component {
  constructor(props) {
    super(props);
  }


  getAlgo = () => {
    const algorithms = this.props.algorithms;
    if(algorithms && algorithms.length) {
      return algorithms.reduce((string,algo) => string + "," + algo, "");
    } else return "None";
  }

  render() {
    return (
        <div id="main">
        <div className="graph">
          <h1> { this.props.graph } </h1>
          <h3> algo checked:  { this.getAlgo() } </h3>
        </div>
          <p> here will be explanation about the graph </p>
        </div>
      );
  }
}

export default Graph;
