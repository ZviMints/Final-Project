import React, { Component } from 'react';
import Algorithms from './Algorithms'

class Results extends Component {
  constructor(props) {
    super(props);
  }

  handleClick() {
    alert("here")
  }

  render() {
    return(
      <div className="results">
      <Algorithms algorithms={this.props.algorithms} updateAlgorithm={this.props.updateAlgorithm} removeAlgorithm={this.props.removeAlgorithm} />
      <button type="button" name="results" onClick={this.handleClick} className="btn btn-primary btn-lg active">Results</button>
      </div>
    );
  }
}
export default Results;
