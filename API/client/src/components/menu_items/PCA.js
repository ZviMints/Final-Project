import React, { Component } from 'react';

class PCA extends Component {
  constructor(props) {
    super(props);
  }

  handleClick =() => {
    this.props.setStep("results")
  }

  render() {
    return(
      <button type="button" name="results" onClick={this.handleClick} className="btn btn-primary btn-lg active">PCA</button>
    );
  }
}
export default PCA;
