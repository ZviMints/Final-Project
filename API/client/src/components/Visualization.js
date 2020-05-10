import React, { Component } from 'react';

import Content from './Content'
import Menu from './Menu'

class Visualization  extends Component {

  constructor(props) {
    super(props);
    this.state = {
      step: "load", // can be load, convert, pca, results
      dataset: "",
      algorithms: []
    }
  }

  // ================ Handlers ================ //
  setStep = (newStep) => { this.setState({step: newStep}) }
  setDataset = (newDataset) => { this.setState({dataset: newDataset})}

  updateAlgorithm = (name) => {
      let clone = [...this.state.algorithms];
      clone.push(name);
      this.setState({algorithms: clone})
  }

  removeAlgorithm = (name) => {
    const newList = this.state.algorithms.filter(algorithm => algorithm !== name)
    this.setState({algorithms: newList})
  }

  // ================ Rendering ================ //
  render() {
        return (
          <div id="visualization">
              <div className="row">
                <div className="menu_column">

                  <Menu
                  step={this.state.step}
                  setStep={this.setStep}
                  dataset={this.state.dataset}
                  algorithms={this.state.algorithms} updateAlgorithm={this.updateAlgorithm} removeAlgorithm={this.removeAlgorithm}
                  setDataset={this.setDataset} />


                </div>
                <div className="content_column">

                <Content
                          step={this.state.step}
                          dataset={this.state.dataset}
                          algorithms={this.state.algorithms}/>
                </div>
              </div>
          </div>
        );
    }
}
export default Visualization;
