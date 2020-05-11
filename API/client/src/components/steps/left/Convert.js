import React, { Component } from 'react';

class Convert extends Component {
  constructor(props) {
    super(props);
    this.state = {
      clicked: false
    }
  }


  handleClick = () => {
    this.props.setStep("pca")
    this.setState({clicked: true})
  }

  render() {
    const renderButton = () => {
      if(this.state.clicked) {
        return <button type="button" className="btn btn-secondary btn-lg">Convert</button>
      }
      else {
        return <button type="button" onClick={this.handleClick} className="btn btn-primary btn-lg active">Convert</button>
      }
    }

    return(
      <div className="convert">
          <h1> Convert </h1>
          {renderButton()}
        </div>
    );
  }
}
export default Convert;
