import React from 'react';
import Spinner from 'react-bootstrap/Spinner'
import Button from 'react-bootstrap/Button'

class Cluster extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      topic: "",
      lock: this.props.getLock()
    }
  }

  setTopicFunction = (topic) => {
    this.setState({ topic: topic })
  }

  render() {
    const information = () => { return <div>{this.state.topic}</div> }
    const loading = () => {
      return (
        <Spinner
                   as="span"
                   animation="border"
                   size="sm"
                   role="status"
                   />
      );
    }


    const renderTagOrProgress = () => {
      if (this.state.topic !== "") return information()
      else if(this.props.getLock()) return null
      else if(!this.props.getLock())    return loading()
    }

    if (!this.props.getLock()) this.props.fetchTopic(this.props.clusters,this.setTopicFunction)
    return (
      <li id={this.state.topic === "" ? "cluster" : "cluster-done"}>
        <div className="row">
          <div className="left">
            {this.props.printArray(this.props.clusters)}
          </div>

          <div className="right">
          {renderTagOrProgress()}
          </div>
        </div>
      </li>
    );
  }
}

export default Cluster;
