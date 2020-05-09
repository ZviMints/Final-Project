
import React, { Component } from 'react';

export default class menu extends Component {



  renderLoad() {
    return (
      <button type="button" className="btn btn-primary btn-lg active">Load</button>
    );
  }

  renderConvert() {
    return (
      <button type="button" className="btn btn-outline-primary mr-2">Convert</button>
    );
  }

  renderPCA() {
    return (
      <button type="button" className="btn btn-outline-primary mr-2">PCA</button>
    );
  }

  renderResults() {
    return (
      <button type="button" className="btn btn-outline-primary mr-2">Results</button>
    );
  }

    render() {
        return (
            <div className="menu">
              { if({this.props.step} === "load") { this.renderLoad() } }
            </div>
          );
    }
}
