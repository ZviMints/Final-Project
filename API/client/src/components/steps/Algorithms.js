
import React, { Component } from 'react';

export default class Algorithms extends Component {
  constructor(props) {
    super(props);
    this.state ={
      connected: true,
      spectral: true,
      kmeans: true
    }
  }

  handleInputChange = (event) => {
    const target = event.target;
    const algorithm = target.name;
    if (target.checked){
      this.props.updateAlgorithm(algorithm);
    } else this.props.removeAlgorithm(algorithm);

    this.setState({
      isChecked: !this.state.isChecked,
    });
  }

  render() {
        return (
            <div className="algorithms">
              <input type="checkbox" defaultChecked={this.state.kmeans} id="algo1" name="kmeans" onChange={this.handleInputChange}/>
              <label htmlFor="kmeans">KMeans</label> <br />

              <input type="checkbox" defaultChecked={this.state.spectral} id="algo2" name="spectral" onChange={this.handleInputChange}/>
              <label htmlFor="spectral">Spectral Clustering</label> <br />

              <input type="checkbox" defaultChecked={this.state.connected} id="algo3" name="connected" onChange={this.handleInputChange}/>
              <label htmlFor="connected">Connected Components</label> <br />
            </div>
          );
    }
}
