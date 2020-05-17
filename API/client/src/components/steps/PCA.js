import React, { Component } from 'react';
import Spinner from 'react-bootstrap/Spinner'
import Button from 'react-bootstrap/Button'
import Badge from 'react-bootstrap/Badge'

class PCA extends Component {
  constructor(props) {
    super(props);
    this.state = {
      clicked: false,
      gotResponse: false,
      IsPCAing: false,
      progressText: "In Progress",
      response: {
        base: ""
      }
    }
  }

// ============================== Handlers ===================================== //
  async fetchPCA() {
    const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ dataset: this.props.getDataset(), useServerData: true })
        };

    const response = await fetch('/pca', requestOptions);
    this.setState({progressText: "Processing Server Data"})

    if (!response.ok) {
      this.setState({clicked: false, IsPCAing: false})
      alert("Server Error")
    }
    else {
      const data = await response.json();
      if(data.err) {
        this.setState({clicked: false, IsPCAing: false})
        alert(data.msg)
      }
      else {
        this.setState({
          response: {
            ...this.state.response,
            base: data.path
          }
        })
        console.log("Server Response: " + this.state.response)
        this.props.setStep("results")
        this.setState({gotResponse: true})

    }
  }
}

handleClick = () => {
    this.setState({clicked: true})
    this.setState({IsPCAing: true})
    this.fetchPCA();
  }

// ============================== Render Main Information ===================================== //
 renderInformation = () => {

  const information = () => {
    return (
       <div id="information">
         <h3><b>Dataset:</b> {this.props.getDataset()} </h3>
         <hr/>
         <h5><b>Base Graph:</b></h5>
         <img src={this.state.response.base} width="950px" height="650px" />
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
        disabled={this.state.IsPCAing}
        onClick={!this.state.IsPCAing ? this.handleClick : null}>
        PCA
      </Button>
    );
 }

 // ============================== Render ===================================== //
  render() {
    return(
      <div className="PCA">
          <div className="column left">
                <h5>Principal component analysis</h5>
                { this.renderButton() }
          </div>
            <div className="column right">
            { this.renderInformation() }
          </div>
      </div>
    );
  }
}
export default PCA;
