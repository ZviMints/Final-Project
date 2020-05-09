import React, { Component } from 'react';

class Load extends Component {
  constructor(props) {
    super(props);
  }

  handleClick() {
    this.props.setStep("convert")
    this.props.setDataset("1")
  }

  render() {
    return(
      <div className="load">
        <h1> Step 1 </h1>
        <hr />
        <h3> Select dataset: </h3>
          <select>
            <option value="1">pan12-sexual-predator-identification-test-corpus-2012-05-17.json</option>
            <option value="2">pan12-sexual-predator-identification-training-corpus-2012-05-01.json</option>
          </select>
        <button type="button" onClick={this.handleClick} className="btn btn-primary btn-lg active">Load</button>
      </div>
    );
  }
}
export default Load;
