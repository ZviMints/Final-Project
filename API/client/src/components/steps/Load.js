import React, { Component } from 'react';
import Spinner from 'react-bootstrap/Spinner'
import Button from 'react-bootstrap/Button'
import Alert from 'react-bootstrap/Alert'
import Form from 'react-bootstrap/Form'

class Load extends Component {
  constructor(props) {
    super(props);
    this.state = {
      dataset : "pan12-sexual-predator-identification-training-corpus-2012-05-01",
      clicked: false,
      isLoading: false,
      progressText: "In Progress",
      gotResponse: false,
      response: {
        before_path: "",
        after_path: "",
        before: "",
        after: "",
        graphData: ""
      }
    }
  }

// ============================== Handlers ===================================== //
  async fetchLoad() {
    const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ dataset: this.state.dataset, useServerData: true })
        };

    const response = await fetch('/load', requestOptions);
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
            before_path: data.before_path,
            after_path: data.after_path,
            before: JSON.stringify(data.before),
            after: JSON.stringify(data.after),
            graphData: data.graphData
          }
        })
        this.props.setStep("embedding")
        this.setState({gotResponse: true})
    }
  }
  }

handleClick = () => {
    this.props.setDataset(this.state.dataset)
    this.setState({clicked: true})
    this.setState({isLoading: true})
    this.fetchLoad();
  }

  handleChange = (event) => {
    if(!this.state.clicked)
      this.setState({ dataset: event.target.value});
  }

// ============================== Render Main Information ===================================== //
 renderInformation = () => {
  const information = () => {
    return (
      <div id="information">
       <h3><b>Dataset:</b> {this.state.dataset} </h3>
       <hr/>

      <div className="row">
      <div className="column left">
          <h4><b>Graph Information:</b></h4>
          <Alert variant="success">
              <b>Before Removing 2-connected componenets: </b> {this.state.response.graphData[0]} <br />
              <b>After Removing 2-connected componenets: </b> {this.state.response.graphData[1]}
           </Alert>
           </div>
      </div>

      <hr/>

       <div className="row">
         <div className="column left">
           <h4><b>Graph as JSON:</b></h4>
           <h5>Before remove 2-connected components</h5>
           <textarea value={this.state.response.before} cols={90} rows={10} />
         </div>
         <div className="column right">
         <br />
         <br />
           <h5>After remove 2-connected components</h5>
           <textarea value={this.state.response.after} cols={90} rows={10} />
         </div>
       </div>

       <hr/>

       <div className="row">
         <div className="column left">
         <h4><b>Visualization:</b></h4>
            <h5>Before remove 2-connected components</h5>
            <img src={this.state.response.before_path} width="450px" height="450px" />
         </div>
         <div className="column right">
         <br />
         <br />
            <h5>After remove 2-connected components</h5>
            <img src={this.state.response.after_path} width="450px" height="450px" />
         </div>
       </div>

   </div>
    );
  }
  const loading = () => {
      if(this.state.clicked)
        return (
          <div>
            <h3><b> { this.state.progressText } <Spinner animation="grow" size="sm"/> <Spinner animation="grow" size="sm"/> <Spinner animation="grow" size="sm"/></b></h3>
         </div>
       );
  }
  if (this.state.gotResponse) return information()
  else                        return loading()
 }

 renderButton = () => {
   return (
      <Button
        variant="primary"
        disabled={this.state.isLoading}
        onClick={!this.state.isLoading ? this.handleClick : null}>
        Load Dataset
      </Button>
    );
}

 // ============================== Render ===================================== //
  render() {
    return(
      <div className="load">
          <div className="column left">
              <h3> Select dataset: </h3>
                <Form.Control as="select">
                <option value="pan12-sexual-predator-identification-training-corpus-2012-05-01">pan12-sexual-predator-identification-training-corpus-2012-05-01</option>
                <option value="pan12-sexual-predator-identification-test-corpus-2012-05-17">pan12-sexual-predator-identification-test-corpus-2012-05-17</option>
                </Form.Control>
                { this.renderButton() }
          </div>
            <div className="column right">
            { this.renderInformation() }
          </div>
      </div>
    );
  }
}
export default Load;
