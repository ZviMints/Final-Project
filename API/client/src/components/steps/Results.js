import React, { Component } from 'react';
import Algorithms from './Algorithms'
import Spinner from 'react-bootstrap/Spinner'
import Button from 'react-bootstrap/Button'
import Badge from 'react-bootstrap/Badge'

class Results extends Component {
  constructor(props) {
    super(props);
    this.state = {
      clicked: false,
      gotResponse: false,
      FetchingData: false,
      progressText: "In Progress",
      algorithms: [],
      response: {
        image: ""
      }
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
    this.setState({progressText: "Processing Server Data"})

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
        this.setState({
          response: {
            ...this.state.response,
            image: data.path
          }
        })
        console.log("Server Response: " + this.state.response)
        this.props.setStep("finished")
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
    return this.state.algorithms.sort((a,b) => a < b).reduce((string,algo) => (string === "") ? algo : string + "+" + algo, "")
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
 renderInformation = () => {

  const information = () => {
    return (
       <div id="information">
         <h3><b>Dataset:</b> {this.props.getDataset()} </h3>
         <hr/>
         <h5><b>Graph:</b></h5>
         <img src={this.state.response.image} width="950px" height="650px" />
       </div>
    );
  }
  const Progress = () => {
      if(this.state.clicked)
        return (
          <div>
          <h3><b> { this.state.progressText } <Spinner animation="grow" size="sm"/> <Spinner animation="grow" size="sm"/> <Spinner animation="grow" size="sm"/></b></h3>
         </div>
       );
  }
  if (this.state.gotResponse) return information()
  else                        return Progress()
 }

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
            { this.renderInformation() }
          </div>
      </div>
    );
  }
}
export default Results;
