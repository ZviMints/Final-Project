import React, { Component } from 'react';
import Algorithms from './Algorithms'

class Results extends Component {
  constructor(props) {
    super(props);
    this.state = {
      clicked: false
    }
  }
  // ================ handleClick ================ //
  handleClick = () => {
    alert("end of the pipline")
    this.setState({clicked: true})
  }
  // ================ Rendering ================ //

  render() {
    const renderButton = () => {
      if(this.state.clicked) {
        return <button type="button" className="btn btn-secondary btn-lg">Results</button>
      }
      else {
        return <button type="button" onClick={this.handleClick} className="btn btn-primary btn-lg active">Results</button>
      }
    }

    return(
      <div className="results">
      <Algorithms updateAlgorithm={this.props.updateAlgorithm} removeAlgorithm={this.props.removeAlgorithm} />
      {renderButton()}
      </div>
    );
  }
}
export default Results;
