import React, { Component, useEffect } from 'react';

class Content extends Component {
  constructor(props) {
    super(props);
  }

  getAlgo = (algorithms) => {
    if(algorithms && algorithms.length) {
      return algorithms.reduce((string,algo) => string + "," + algo, "");
    } else return "None";
  }

  render() {
    return (
        <div id="main">
        <div className="graph">
          <h1> { this.props.graph } </h1>
          <h1> { this.props.algorithms } </h1>
          <h3> algo checked:  { this.getAlgo(this.props.algorithms) } </h3>
        </div>
          <p> here will be explanation about the graph </p>
        </div>
      );
  }
}

export default Content;
