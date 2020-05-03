
import React, { Component } from 'react';

export default class Algorithms extends Component {
    render() {
        return (
            <div className="algorithms">
              <h4> Algorithms: </h4>
              <input type="checkbox" id="algo1" name="kmeans"/>
              <label htmlFor="kmeans">KMeans</label> <br />

              <input type="checkbox" id="algo2" name="spectral_clustering"/>
              <label htmlFor="spectral_clustering">Spectral Clustering</label> <br />

              <input type="checkbox" id="algo3" name="connected_components"/>
              <label htmlFor="connected_components">Connected Components</label> <br />
            </div>
          );
    }
}
