import React, { Component } from 'react';
import Spinner from 'react-bootstrap/Spinner'

class Load extends Component {
  constructor(props) {
    super(props);
    this.state = {
      dataset : "pan12-sexual-predator-identification-training-corpus-2012-05-01",
      clicked: false,
      gotResponse: false,
      response: {
        before_path: "",
        after_path: "",
        before: "",
        after: ""
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
            after: JSON.stringify(data.after)
          }
        })
        this.setState({gotResponse: true})
        this.props.setStep("convert")
    }
  }
  }

handleClick = () => {
    this.props.setDataset(this.state.dataset)
    this.setState({clicked: true})
    this.fetchLoad();
  }

  handleChange = (event) => {
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
           <h3><b>In Progress <Spinner animation="grow" size="sm"/> <Spinner animation="grow" size="sm"/> <Spinner animation="grow" size="sm"/></b></h3>
         </div>
       );
  }
  if (this.state.gotResponse) return information()
  else                        return loading()
 }

 renderButton = () => {
     return (this.state.clicked) ? <button type="button" className="btn btn-secondary btn-lg">Load</button> : <button type="button" onClick={this.handleClick} className="btn btn-primary btn-lg active">Load</button>
 }

 // ============================== Render ===================================== //
  render() {
    return(
      <div className="load">
          <div className="column left">
              <h3> Select dataset: </h3>
                <select value={this.state.dataset} onChange={this.handleChange}>
                <option value="pan12-sexual-predator-identification-training-corpus-2012-05-01">pan12-sexual-predator-identification-training-corpus-2012-05-01</option>
                  <option value="pan12-sexual-predator-identification-test-corpus-2012-05-17">pan12-sexual-predator-identification-test-corpus-2012-05-17</option>
                </select>
                <br />
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
