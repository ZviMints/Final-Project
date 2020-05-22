import React, { Component } from 'react';
import Algorithms from './Algorithms'
import Button from 'react-bootstrap/Button'
import Badge from 'react-bootstrap/Badge'
import Form from 'react-bootstrap/Form'
import Nav from 'react-bootstrap/Nav'
import Tabs from 'react-bootstrap/Tabs'
import Tab from 'react-bootstrap/Tab'

class BERT extends Component {
  constructor(props) {
    super(props);
    this.state = {
      clicked: false,
      gotResponse: false,
      FetchingData: false,
      key: "by_algo",
      algorithms: [],
      image: "/data/pca/" + this.props.getDataset() + "/base.png"
    }
  }

// ============================== Handlers ===================================== //
  async fetchBERT() {
    const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ dataset: this.props.getDataset(), algorithms: this.parseAlgoToString() })
        };

    const response = await fetch('/bert', requestOptions);

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
    this.fetchBERT();
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
  setKey = (key) => {
    this.setState({key: key})
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


renderByAlgo = () => {
  const algo = "kmeans"
  return (
    <div>
    <Form>
      <Form.Group controlId="exampleForm.ControlSelect1">
        <Form.Label><b><h5>Relevant Algorithm</h5></b></Form.Label>
        <Form.Control as="select">
          <option>KMeans</option>
          <option>Connected Components</option>
          <option>Spectral Clustering</option>
        </Form.Control>
      </Form.Group>
      <Form.Group controlId="exampleForm.ControlSelect2">
      <Form.Label><b><h5>KMeans</h5></b></Form.Label>
        <Form.Control as="select" multiple>
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
          <option>5</option>
        </Form.Control>
      </Form.Group>

      <Button variant="primary" type="submit">
      Show Topics
    </Button>
    </Form>
    </div>
  );
}

renderIntersection = () => {
  return (
    <div>
    <Form>
      <Form.Group controlId="exampleForm.ControlSelect2">
      <Form.Label><b><h5>KMeans</h5></b></Form.Label>
        <Form.Control as="select" multiple>
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
          <option>5</option>
        </Form.Control>
      </Form.Group>
      <Form.Group controlId="exampleForm.ControlSelect2">
      <Form.Label><b><h5>Connected Components</h5></b></Form.Label>
        <Form.Control as="select" multiple>
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
          <option>5</option>
        </Form.Control>
      </Form.Group>
      <Form.Group controlId="exampleForm.ControlSelect2">
      <Form.Label><b><h5>Spectral Clustering</h5></b></Form.Label>
        <Form.Control as="select" multiple>
          <option>1</option>
          <option>2</option>
          <option>3</option>
          <option>4</option>
          <option>5</option>
        </Form.Control>
      </Form.Group>

     <Button variant="primary" type="submit">Show Topics</Button>{' '}
     <Button variant="danger">Reset</Button>{' '}

    </Form>
    </div>
  );
}


renderBertMenu = () => {
  return (
    <Tabs id="menu" activeKey={this.state.key} onSelect={(k) => this.setKey(k)}>
      <Tab eventKey="by_algo" title="By Cluster Algorithm">
      <br />
      {this.renderByAlgo()}
      </Tab>
      <Tab eventKey="intersection" title="Clusters Intersection">
      <br />
      {this.renderIntersection()}
      </Tab>
    </Tabs>
  );
}
 // ============================== Render ===================================== //
  render() {
    return(
      <div className="BERT">
          <div className="column left">
                <b><h4>BERT</h4></b>
                <hr />
                { this.renderBertMenu() }
          </div>
            <div className="column right">
            <div id="information">
              <h3><b>Dataset:</b> {this.props.getDataset()} </h3>
              <hr/>
              <h5><b>Dictionary:</b></h5>
              <h4> <Badge variant="success">Connected-Components Clustering</Badge> <Badge variant="danger">KMeans Clustering</Badge> <Badge variant="warning">Spectral Clustering</Badge> <Badge variant="primary">Nodes</Badge> </h4>
              <hr />
              <img src={this.state.image} width="950px" height="650px" />
            </div>
          </div>
      </div>
    );
  }
}
export default BERT;
