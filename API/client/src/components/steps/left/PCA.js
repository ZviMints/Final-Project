import React, { Component } from 'react';

class PCA extends Component {
  constructor(props) {
    super(props);
    this.state = {
      clicked: false
    }
  }

  handleClick =() => {
    this.props.setStep("results")
    this.setState({clicked: true})
  }

  render() {
    const renderButton = () => {
      if(this.state.clicked) {
        return <button type="button" className="btn btn-secondary btn-lg">PCA</button>
      }
      else {
        return <button type="button" onClick={this.handleClick} className="btn btn-primary btn-lg active">PCA</button>
      }
    }
    return(
      <div id="pca">
        { renderButton() }
      </div>
    );
  }
}
export default PCA;
