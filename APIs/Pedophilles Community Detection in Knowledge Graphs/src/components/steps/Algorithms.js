
import React, { Component } from 'react';

export default class Algorithms extends Component {
  constructor(props) {
    super(props);
  }

  handleInputChange = (event) => {
    const target = event.target;
    const algorithm = target.name;
    if (target.checked){
      this.props.updateAlgorithm(algorithm);
    } else this.props.removeAlgorithm(algorithm);
  }

  render() {
        return (
            <div className="algorithms">
              <input type="checkbox" className="checkbox" id="algo1" name="kmeans" onChange={this.handleInputChange}/>{'   '}
              <label htmlFor="kmeans">KMeans</label> <br />

              <input type="checkbox"  className="checkbox" id="algo2" name="spectral" onChange={this.handleInputChange}/>{'   '}
              <label htmlFor="spectral">Spectral Clustering</label> <br />

              <input type="checkbox"  className="checkbox" id="algo3" name="connected" onChange={this.handleInputChange}/>{'   '}
              <label htmlFor="connected">Connected Components</label> <br />
            </div>
          );
    }
}
