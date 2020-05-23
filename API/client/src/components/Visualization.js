import React, { Component } from 'react';

import FlipMove from "react-flip-move";

import Load from './steps/Load'
import Embedding from './steps/Embedding'
import PCA from './steps/PCA'
import Results from './steps/Results'
import BERT from './steps/BERT'


class Visualization  extends Component {

  constructor(props) {
    super(props);
    this.state = {
      steps: ["load"],
      dataset: ""
    }

    this.total_states = ["load","embedding","pca","results", "bert"];

    this.map = new Map();
    this.map.set("load",<Load setStep={this.setStep} setDataset={this.setDataset}/>);
    this.map.set("embedding",<Embedding setStep={this.setStep} getDataset={this.getDataset}/>);
    this.map.set("pca",<PCA setStep={this.setStep} getDataset={this.getDataset}/>);
    this.map.set("results",<Results setStep={this.setStep} getDataset={this.getDataset} />);
    this.map.set("bert",<BERT getDataset={this.getDataset} />);
  }

// ================ Scrolling ================ //

componentDidMount(){
    const node = this.refs.trackerRef;
    node && node.scrollIntoView({block: "end", behavior: 'smooth'})
  }
  componentDidUpdate() {
    const node = this.refs.trackerRef;
    node && node.scrollIntoView({block: "end", behavior: 'smooth'})
  }

  // ================ Handlers ================ //
  getDataset = () => {
    return this.state.dataset
   }


  setStep = (newStep) => {
    let clone = [...this.state.steps];
    clone.push(newStep);
    this.setState({steps: clone})
   }

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
    const all_divs = this.state.steps.map( (step,index) => {
    return (
      <div id="row" key={index}>
      { this.map.get(step) }
      </div>
    );
    }
   )

    const all_others = () => { return (
      <div className="other_buttons">
      <h4>Next Steps: </h4>
      {                       this.total_states
                              .filter(step => ! this.state.steps.includes(step))
                              .map((step,index) => <button key={index} id="button" onClick={() => alert("step '" + step + "' cannot be completed yet, following the previous steps")} type="button" name="results"  key={index}  className="btn btn-secondary">{step.charAt(0).toUpperCase() + step.slice(1)}</button>)

      }
      </div>
    );
  }
  // Main Return function
  return (
    <div>
          <div id="visualization">
          <FlipMove easing="ease-in">
                { all_divs }
          </FlipMove>
          <div style={{height: '1px'}} id='#tracker' ref="trackerRef"></div>
          { (!this.state.steps.includes("results")) ? all_others() : null  }
          </div>
    </div>
    );
  }
}
export default Visualization;
