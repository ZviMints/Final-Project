
import React, { Component } from 'react';


import Load from './menu_items/Load'
import Convert from './menu_items/Convert'
import PCA from './menu_items/PCA'
import Results from './menu_items/Results'


class Menu  extends Component {
  constructor(props) {
    super(props);
  }

  renderItem = () => {
    if(this.props.step === "load") { return <Load setStep={this.props.setStep} setDataset={this.props.setDataset} /> } // Need to fix that problem
    else if(this.props.step === "convert") { return <Convert />}
    else if(this.props.step === "pca") { return  <PCA /> }
    else if(this.props.step === "results") { return <Results algorithms={this.props.algorithms} updateAlgorithm={this.props.updateAlgorithm} removeAlgorithm={this.props.removeAlgorithm} /> }
  }

  render() {
      // Main render function
      return (
        <div className="menu">
            { this.renderItem() }
        </div>
    );
  }
}
export default Menu;
