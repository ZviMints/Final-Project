import React, { Component, useRef, useEffect } from 'react';

import FlipMove from "react-flip-move";

import Right_Load from './steps/right/Load'
import Right_Convert from './steps/right/Convert'
import Right_PCA from './steps/right/PCA'
import Right_Results from './steps/right/Results'

import Left_Load from './steps/left/Load'
import Left_Convert from './steps/left/Convert'
import Left_PCA from './steps/left/PCA'
import Left_Results from './steps/left/Results'

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
    this.map.set("load",        { "left": <Left_Load steps={this.state.steps} setStep={this.setStep} setDataset={this.setDataset} />,
                                  "right": <Right_Load /> }
                                );

    this.map.set("convert",     { "left": <Left_Convert steps={this.state.steps} setStep={this.setStep} dataset={this.state.dataset}  />,
                                  "right": <Right_Convert dataset={this.state.dataset} /> }
                                );

    this.map.set("pca",         { "left": <Left_PCA steps={this.state.steps} setStep={this.setStep}/>,
                                  "right": <Right_PCA /> }
                                );

    this.map.set("results",     { "left": <Left_Results steps={this.state.steps} setStep={this.setStep} removeAlgorithm ={this.removeAlgorithm}  updateAlgorithm = {this.updateAlgorithm} />,
                                  "right": <Right_Results algorithms={this.state.algorithms} /> }
                                );
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
    const place = (index % 2 === 0) ? 'even' : 'odd';
    const last_index = (index === this.state.steps.length - 1);
      return (
        <div id="row" className={place}>
            <div id="column"> { this.map.get(step).left } </div>
            <div id="column"> { this.map.get(step).right } </div>
        </div>
      );
    }
   )

    const all_others = () => { return (
      <div className="other_buttons">
      <hr />
      <h4>Next Steps: </h4>
      {                       this.total_states
                              .filter(step => ! this.state.steps.includes(step))
                              .map(step => <button id="button" onClick={() => alert("step '" + step + "' cannot be completed yet, following the previous steps")} type="button" name="results" className="btn btn-secondary">{step.charAt(0).toUpperCase() + step.slice(1)}</button>)

      }
      </div>
    );
  }
  // Main Return function
  return (
          <div id="visualization">
          <FlipMove duration={700} easing="ease-out">
                { all_divs }
          </FlipMove>
          { all_others() }
          <div style={{height: '30px'}} id='#tracker' ref="trackerRef"></div>
          </div>
    );
  }
}
export default Visualization;
