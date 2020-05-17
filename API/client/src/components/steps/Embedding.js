import React, { Component } from 'react';
import Spinner from 'react-bootstrap/Spinner'
import Button from 'react-bootstrap/Button'
import Badge from 'react-bootstrap/Badge'
import Modal from 'react-bootstrap/Modal'

class Embedding extends Component {
  constructor(props) {
    super(props);
    this.state = {
      clicked: false,
      gotResponse: false,
      isEmbedding: false,
      isOpen: false,
      progressText: "In Progress",
      response: {
        walk_length: 0,
        num_walks: 0,
        walks: ""
      }
    }
  }

// ============================== Handlers ===================================== //
  async fetchEmbedding() {
    const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ dataset: this.props.getDataset(), useServerData: false })
        };

    const response = await fetch('/embedding', requestOptions).catch(ex => alert("Timeout with ex: " + ex));
    this.setState({progressText: "Processing Server Data"})

    if (!response.ok) {
      this.setState({clicked: false})
      alert("Server Error")
    }
    else {
      const data = await response.json();
      if(data.err) {
        this.setState({clicked: false})
        alert(data.msg)
      }
      else {
        this.setState({
          response: {
            ...this.state.response,
            walks: data.walks,
            num_walks: data.num_walks,
            walk_length: data.walk_length
          }
        })
        console.log("Server Response: " + this.state.response)
        this.props.setStep("pca")
        this.setState({gotResponse: true})
    }
  }
  }

handleClick = () => {
    this.setState({clicked: true})
    this.setState({isEmbedding: true})
    this.fetchEmbedding();
  }

 handleClose = () => { this.setState({isOpen: false}); }
 handleShow = () => { this.setState({isOpen: true}); }

// ============================== Render Main Information ===================================== //
 renderInformation = () => {

  const information = () => {
    return (
       <div id="information">
         <h3><b>Dataset:</b> {this.props.getDataset()} </h3>
         <hr/>
         <h4><b>Walks Generated:</b></h4>
         <h5><b>{this.state.response.walk_length}</b> Number of nodes in each walk</h5>
         <h5><b>{this.state.response.num_walks}</b> Number of walks per node</h5>

         <div>
           <Button onClick={this.handleShow} variant="outline-primary">Checkout Generated Walks</Button>

                 <Modal show={this.state.isOpen} onHide={this.handleClose}>
                   <Modal.Header closeButton>
                     <Modal.Title>Walks</Modal.Title>
                    <Button variant="secondary" onClick={this.handleClose}>
                         Close
                    </Button>
                   </Modal.Header>
                   <Modal.Body>{this.state.response.walks}</Modal.Body>
                 </Modal>
         </div>

         <h5>Nodes Embedded <Badge variant="success">Successfully</Badge></h5>
       </div>
    );
  }
  const Embeddinging = () => {
      if(this.state.clicked)
        return (
          <div>
          <h3><b> { this.state.progressText } <Spinner animation="grow" size="sm"/> <Spinner animation="grow" size="sm"/> <Spinner animation="grow" size="sm"/></b></h3>
         </div>
       );
  }
  if (this.state.gotResponse) return information()
  else                        return Embeddinging()
 }

 renderButton = () => {
   return (
      <Button
        variant="primary"
        disabled={this.state.isEmbedding}
        onClick={!this.state.isEmbedding ? this.handleClick : null}>
        Embedding
      </Button>
    );
 }

 // ============================== Render ===================================== //
  render() {
    return(
      <div className="Embedding">
          <div className="column left">
                <h5>Generate Random Walks & Embedding</h5>
                { this.renderButton() }
          </div>
            <div className="column right">
            { this.renderInformation() }
          </div>
      </div>
    );
  }
}
export default Embedding;
