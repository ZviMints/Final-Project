
import React, { Component } from 'react';

export default class Algorithms extends Component {
  constructor(props) {
    super(props);
  }

  handleChange = (event) => {
    const target = event.target;
    alert(target);
  }

  handleInputChange = (event) => {
    const target = event.target;
    const algorithm = target.name;
    if (target.checked){
      let clone = [...this.props.algorithms];
      clone.push(algorithm);
      this.props.updateList(clone);
    } else this.props.remoteItem(algorithm);
  }

  render() {
        return (
            <div className="algorithms">
              <h4> Algorithms: </h4>
              <input type="checkbox" id="algo1" name="kmeans" onChange={this.handleInputChange}/>
              <label htmlFor="kmeans">KMeans</label> <br />

              <input type="checkbox" id="algo2" name="spectral_clustering" onChange={this.handleInputChange}/>
              <label htmlFor="spectral_clustering">Spectral Clustering</label> <br />

              <input type="checkbox" id="algo3" name="connected_components" onChange={this.handleInputChange}/>
              <label htmlFor="connected_components">Connected Components</label> <br />
            </div>
          );
    }
}
