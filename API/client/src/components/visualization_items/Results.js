import React, { Component } from 'react';

class Results extends Component {
  render() {
    return(
      <div className="vis_convert">
          <div className="graph">
            <h1> { this.props.graph } </h1>
            <h1> { this.props.algorithms } </h1>
          </div>
          <p> here will be explanation about the graph </p>
      </div>
    );
  }
}
export default Results;
