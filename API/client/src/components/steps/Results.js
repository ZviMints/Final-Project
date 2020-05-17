import React, { Component } from 'react';
import Algorithms from './Algorithms'
import Button from 'react-bootstrap/Button'
import Badge from 'react-bootstrap/Badge'

class Results extends Component {
  constructor(props) {
    super(props);
    this.state = {
      clicked: false,
      gotResponse: false,
      FetchingData: false,
      algorithms: [],
      image: "/data/pca/" + this.props.getDataset() + "/base.png"
    }
  }

// ============================== Handlers ===================================== //
  async fetchResults() {
    const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ dataset: this.props.getDataset(), algorithms: this.parseAlgoToString() })
        };

    const response = await fetch('/results', requestOptions);

    if (!response.ok) {
      this.setState({clicked: false, FetchingData: false})
      alert("Server Error")
    }
    else {
      const data = await response.json();
      if(data.err) {
        this.setState({clicked: false, FetchingData: false})
        alert(data.msg)
      }
      else {
        this.setState({image: data.path})
        console.log("Image State: " + this.state.image)
        this.setState({gotResponse: true})
        this.setState({FetchingData: false})

    }
  }
  }

handleClick = () => {
    this.setState({clicked: true})
    this.setState({FetchingData: true})
    this.fetchResults();
  }

  // ============================== algorithms ===================================== //
  parseAlgoToString = () => {
    if(this.state.algorithms.length === 0) return "base"
    return this.state.algorithms.sort().reduce((string,algo) => (string === "") ? algo : string + "+" + algo, "")
  }

  updateAlgorithm = (name) => {
       let clone = [...this.state.algorithms];
       clone.push(name);
       this.setState({algorithms: clone})
   }

   removeAlgorithm = (name) => {
     const newList = this.state.algorithms.filter(algorithm => algorithm !== name)
     this.setState({algorithms: newList})
   }

// ============================== Render Main Information ===================================== //
 renderButton = () => {
   return (
      <Button
        variant="primary"
        onClick={!this.state.FetchingData ? this.handleClick : null}>
        Show Graph
      </Button>
    );
 }


 // ============================== Render ===================================== //
  render() {

    return(
      <div className="Results">
          <div className="column left">
                <b><h4>Results</h4></b>
                <hr />
                <h5>Check which algorithm to show: </h5>
                <Algorithms updateAlgorithm={this.updateAlgorithm} removeAlgorithm={this.removeAlgorithm} />
                { this.renderButton() }
          </div>
            <div className="column right">
            <div id="information">
              <h3><b>Dataset:</b> {this.props.getDataset()} </h3>
              <hr/>
              <h5><b>Algorithms:</b> {this.parseAlgoToString()}</h5>
              <h5><b>Image:</b> {this.state.image} </h5>
              <img src={this.state.image} width="950px" height="650px" />
              <br />
              <h5><b>Dictionary:</b></h5>
              <h5><Badge variant="success">Connected-Components Clustering</Badge></h5>
              <h5><Badge variant="danger">KMeans Clustering</Badge></h5>
              <h5><Badge variant="warning">Clustering Clustering</Badge></h5>
              <h5><Badge variant="primary">Nodes</Badge></h5>
            </div>
          </div>
      </div>
    );
  }
}
export default Results;
