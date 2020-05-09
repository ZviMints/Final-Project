import React, { Component } from 'react';

class Convert extends Component {
  constructor(props) {
    super(props);
  }

  handleClick() {
    alert("here")
  }

  render() {
    return(
      <button type="button" name="results" onClick={this.handleClick} className="btn btn-primary btn-lg active">Convert</button>
    );
  }
}
export default Convert;
