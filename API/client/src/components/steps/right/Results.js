import React, { Component } from 'react';

class Results extends Component {
  render() {
    return(
      <div className="vis_convert">
            <h1> Algorithms: { this.props.algorithms } </h1>
            <p> here will be explanation about the graph </p>
      </div>
    );
  }
}
export default Results;
