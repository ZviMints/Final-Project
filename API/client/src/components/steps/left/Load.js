import React, { Component } from 'react';

class Load extends Component {
  constructor(props) {
    super(props);
    this.state = {
      dataset : "pan12-sexual-predator-identification-test-corpus-2012-05-17.json",
    }
  }

  handleClick = () => {
    this.props.setDataset(this.state.dataset)
    this.props.setStep("convert")
  }

  handleChange = (event) => {
    this.setState({ dataset: event.target.value});
  }

  render() {
    const renderButton = () => {
      if(this.props.steps.includes("convert")) {
        return <button type="button" className="btn btn-secondary btn-lg">Load</button>
      }
      else {
        return <button type="button" onClick={this.handleClick} className="btn btn-primary btn-lg active">Load</button>
      }
    }

    return(
      <div className="load">
        <h3> Select dataset: </h3>
          <select value={this.state.dataset} onChange={this.handleChange}>
            <option value="pan12-sexual-predator-identification-test-corpus-2012-05-17.json">pan12-sexual-predator-identification-test-corpus-2012-05-17.json</option>
            <option value="pan12-sexual-predator-identification-training-corpus-2012-05-01.json">pan12-sexual-predator-identification-training-corpus-2012-05-01.json</option>
          </select>
          <br />
          { renderButton() }
      </div>
    );
  }
}
export default Load;
