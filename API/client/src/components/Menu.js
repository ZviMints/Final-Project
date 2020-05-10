
import React, { Component } from 'react';


import Load from './menu_items/Load'
import Convert from './menu_items/Convert'
import PCA from './menu_items/PCA'
import Results from './menu_items/Results'


class Menu extends Component {

  constructor(props) {
    super(props)
  };

  renderStep = (step) => {
    switch (step) {
      case "load":
      return (
           <Load
           setStep={this.props.setStep}
           setDataset={this.props.setDataset} />);
      case "convert":
        return (
          <Convert
            setStep={this.props.setStep}
            dataset={this.props.dataset} />
          );
      case "pca":
        return (
         <PCA
          setStep={this.props.setStep} />
        );
      case "results":
      return (
        <Results
        algorithms={this.props.algorithms}
        updateAlgorithm={this.props.updateAlgorithm}
        removeAlgorithm={this.props.removeAlgorithm} /> );
      default:
        alert("unknown step")

    }
  }

  render() {
      // Main render function
      return (
        <div className="menu">
             { this.renderStep(this.props.step) }
        </div>
    );
  }
}
export default Menu;
