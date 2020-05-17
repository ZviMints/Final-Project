import React, { Component, useRef, useEffect } from 'react';

import FlipMove from "react-flip-move";

import Load from './steps/Load'
import Convert from './steps/Convert'
import PCA from './steps/PCA'
import Results from './steps/Results'


class Visualization  extends Component {

  constructor(props) {
    super(props);
    this.state = {
      steps: ["load"],
      dataset: "",
      algorithms: []
    }

    this.total_states = ["load","convert","pca","results"];

    this.map = new Map();
    this.map.set("load",<Load setStep={this.setStep} setDataset={this.setDataset}/>);
    this.map.set("convert",<Convert setStep={this.setStep} dataset={this.state.dataset}/>);
    this.map.set("pca",<PCA setStep={this.setStep} dataset={this.state.dataset}/>);
    this.map.set("results",<Results />);
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
          <div id="visualization">
          <FlipMove easing="ease-in">
                { all_divs }
          </FlipMove>
          <div style={{height: '1px'}} id='#tracker' ref="trackerRef"></div>
          { all_others() }
          </div>
    );
  }
}
export default Visualization;
