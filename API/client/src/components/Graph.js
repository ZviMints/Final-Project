import React, { Component } from 'react';

class Graph extends Component {
  constructor(props) {
    super(props);
  }

// This method is responsoible to render header above the graph
renderHeader = () => {

  const getAlgo = () => {

    const algorithms = this.props.algorithms;

    const combiner = (string) => {
      if(string === "") return "";
      else return ", ";
    }

    if(algorithms && algorithms.length) {
      return algorithms.reduce((string,algo) => string + combiner(string) + algo, "");
    } else return "None";
  }

  return (
    <div>
      <h1> Graph </h1>
      <h2> Cool Description </h2>
      <h3> Algorithms: {getAlgo()}</h3>
    </div>
  );
}

  // This is the main render function
  render() {
    return (
        <div id="main">
         { this.renderHeader() }
         <div className="graph">
            <img src={'data:image/png;base64,' + this.props.graph_path} />
          </div>
          { this.renderDescription() }
        </div>
      );
  }

  // This method is responsoible to render description bellow the graph
  renderDescription = () => {
    return  <p> here will be explanation about the graph </p>
  }

}

export default Graph;
