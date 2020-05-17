import React, { Component } from 'react';

class PCA extends Component {
  constructor(props) {
    super(props);
    this.state = {
      clicked: false
    }
  }

  // ============================== Handlers ===================================== //
  handleClick = () => {
    this.props.setStep("results")
    this.setState({clicked: true})
  }
  // ============================== Render Main Information ===================================== //
   renderInformation = () => {
     if(this.state.clicked) {
       return (
         <div>
           <h3>test_full:</h3>
           <img src="./models/load/test_full.jpg" width="450px" height="450px" />
           <hr />
           <h3>test_after_remove:</h3>
           <img src="./models/load/test_after_remove.png" width="450px" height="450px" />
       </div>
      );
     }
   }

  renderButton = () => {
       return (this.state.clicked) ? <button type="button" className="btn btn-secondary btn-lg">Results</button> : <button type="button" onClick={this.handleClick} className="btn btn-primary btn-lg active">Results</button>
   }

  // ============================== Render ===================================== //
  render() {
    return(
      <div className="convert">
      <div id="row">
            <div className="column left">
                    { this.renderButton() }
              </div>
            <div className="column right">
                  { this.renderInformation() }
              </div>
          </div>
        </div>
    );
  }
}
export default PCA;
