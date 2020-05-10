import React, { Component } from 'react';

class Convert extends Component {
  constructor(props) {
    super(props);
  }

  handleClick = () => {
    this.props.setStep("pca")
  }

  render() {
    return(
      <div className="convert">
          <h1> Convert </h1>
          <button type="button" name="results" onClick={this.handleClick} className="btn btn-primary btn-lg active">Convert</button>
        </div>
    );
  }
}
export default Convert;
