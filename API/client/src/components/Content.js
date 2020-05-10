import React, { Component, useEffect } from 'react';



import Load from './visualization_items/Load'
import Results from './visualization_items/Results'
import PCA from './visualization_items/PCA'
import Convert from './visualization_items/Convert'

class Content extends Component {
  constructor(props) {
    super(props);
  }

  getAlgo = (algorithms) => {
    if(algorithms && algorithms.length) {
      return algorithms.reduce((string,algo) => string + "," + algo, "");
    } else return "None";
  }


  renderByStep = (step) => {
    switch (step) {
      case "load": return (<Load />);
      case "convert": return (
        <Convert
         dataset={this.props.dataset}  />
      );
      case "pca": return (<PCA />);
      case "results": return (<Results algorithms={this.props.algorithms} />)
      default: alert("unknown Visualization item")
    }
  }


  render() {
    return (
        <div id="steps_visualization">
        { this.renderByStep(this.props.step) }
        </div>
      );
  }
}

export default Content;
