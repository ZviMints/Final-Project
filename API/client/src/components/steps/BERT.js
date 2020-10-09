import React, { Component } from 'react';
import Button from 'react-bootstrap/Button'
import Badge from 'react-bootstrap/Badge'
import Tabs from 'react-bootstrap/Tabs'
import Tab from 'react-bootstrap/Tab'
import Spinner from 'react-bootstrap/Spinner'
import Cluster from './Cluster'
import Form from 'react-bootstrap/Form'
import Alert from 'react-bootstrap/Alert'

class BERT extends Component {
  constructor(props) {
    super(props);
    this.state = {
      gotAllLabels: false,
      labels: [],
      fetchingAllLabels: false,
      key: "all",
      option_cluster: "",
      option_topic: "",
      lock: true,
      show_option_answer:false,
      image: "/data/pca/" + this.props.getDataset() + "/connected+kmeans+spectral.png"
    }
    {this.fetchAllLabels()}
  }

// ============================== Handlers ===================================== //
  async fetchAllLabels() {
    const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ dataset: this.props.getDataset(), useServerData: false})
        };
    const response = await fetch('/getLabels', requestOptions);
    if (!response.ok) {
      this.setState({gotAllLabels: false, fetchingAllLabels: false})
      alert("Server Error")
    }
    else {
      const data = await response.json();
      if(data.err) {
        this.setState({gotAllLabels: false, fetchingAllLabels: false})
        alert(data.msg)
      }
      else {
        this.setState({labels: data.labels})
        this.setState({option_cluster: data.labels.filter(arr => arr.length !== 0)[0]})
        console.log("labels: " + this.state.labels)
        this.setState({gotAllLabels: true,  fetchingAllLabels: true})
    }
  }
}
  async fetchTopic(cluster, setFunction) {
    const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ dataset: this.props.getDataset(), useServerData: false, cluster: cluster})
        };
    const response = await fetch('/bert', requestOptions);
    if (!response.ok) {
      alert("Server Error")
    }
    else {
      const data = await response.json();
      if(data.err) {
        alert(data.msg)
      }
      else {
        console.log("running setFunction with topic: " + data.topic)
        setFunction(data.topic)
    }
  }
}

handleClick = () => {
    this.setState({clicked: true})
    this.setState({FetchingData: true})
    this.fetchBERT();
  }

  setKey = (key) => {
    this.setState({key: key})
  }

  handleChange(event) {
    this.setState({option_cluster: event.target.value});
  }

setOptionTopic = (topic) => {
  this.setState({ option_topic: topic })
}
  handleSubmit = (event) => {
    this.setState({show_option_answer:true})
    this.fetchTopic(this.state.option_cluster,this.setOptionTopic);
}

// ============================== Render Main Information ===================================== //
  printArray = (arr) => {
    return "[" + arr.map(key => " " + key) + " ]"
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

handleLockButton = () => {
  this.setState({lock:false})
}

getLock = () => { return this.state.lock }


findAllClusters = () => {
  const information = () => {
    return (
      <ul id="clusters">
      <Button
      className="lockButton"
      onClick={this.state.lock ? this.handleLockButton : null}
      variant="outline-dark"
      disabled={this.state.lock ? false : true}
      > Fetch Data </Button>
      <div className="row">
        <div className="left"><b>Clusters</b></div>
        <div className="right"><b>Topic</b></div>
      </div>
        { this.state.labels.filter(arr => arr.length !== 0).map(clusters => <Cluster getLock={this.getLock} printArray={this.printArray} key={clusters} props={this.props} fetchTopic={this.fetchTopic} clusters = {clusters} /> )}
      </ul>
  );
}
  const loading = () => { return <Spinner animation="border" /> }

  if (this.state.gotAllLabels) return information()
  else                         return loading()
}

findSpecificCluster = () => {
  const renderAnswerForTopic = () => {
    return (
      <div className="topic_response">
      <Alert variant="warning">
      <b>Topic: </b> {this.state.option_topic === "" ? <Spinner animation="border" /> : this.state.option_topic}
      </Alert>
      </div>
  );
  }

  const loading = () => { return <Spinner animation="border" /> }
  const information = () => {
  return (
    <div>
    <Form>
      <Form.Group controlId="exampleForm.SelectCustom">
        <Form.Label><b>Select Clusters Intersection</b></Form.Label>
        <Form.Control as="select" custom>
        <option disabled>Select Intersection</option>
          {this.state.labels.filter(arr => arr.length !== 0).map(cluster => <option key={cluster} onChange={this.handleChange} key={cluster}>{this.printArray(cluster)}</option>)}
        </Form.Control>
      </Form.Group>
      <Button
      onClick={!this.state.show_option_answer ? this.handleSubmit : null}
      variant="primary"
      disabled={!this.state.show_option_answer ? false : true}
      >
        Submit
      </Button>
      </Form>

    {this.state.show_option_answer ? renderAnswerForTopic() : null}
    </div>
  );
  }

  if (this.state.gotAllLabels) return information()
  else                         return loading()
}


renderBertMenu = () => {
  return (
    <Tabs id="menu" activeKey={this.state.key} onSelect={(k) => this.setKey(k)}>
      <Tab eventKey="specific" title="Find Specific Topic">
      <br />
      {this.findSpecificCluster()}
      </Tab>
      <Tab eventKey="all" title="All Clusters">
      <br />
      {this.findAllClusters()}
      </Tab>
    </Tabs>
  );
}
 // ============================== Render ===================================== //
  render() {
    return(
      <div className="bert">
          <div className="left">
                <b><h4>BERT</h4></b>
                <hr />
                { this.renderBertMenu() }
          </div>
            <div className="right">
            <div id="bert information">
            <img src={this.state.image} width="950px" height="650px" />
            </div>
          </div>
      </div>
    );
  }
}
export default BERT;
