import React, { Component } from 'react';

class Convert extends Component {
  checkIfTrain = (string) => { return string.includes("train") }
  renderScreen = (dataset) => {
    const train = this.checkIfTrain(dataset)
    if(train) {
        return (
          <div>
            <h3>test_full:</h3>
            <img src="./models/load/test_full.jpg" width="450px" height="450px" />
            <hr />
            <h3>test_after_remove:</h3>
            <img src="./models/load/test_after_remove.png" width="450px" height="450px" />
          </div>
        );
    } else {
      return (
        <div>
              <div class="row">
                <div class="column">
                  <h3>train_full:</h3>
                  <img src="./models/load/train_full.jpg" width="450px" height="450px" />
                </div>
                <div class="column">
                  <h3>train_after_remove:</h3>
                  <img src="./models/load/train_after_remove.png" width="450px" height="450px" />
                </div>
              </div>
        </div>
      );
    }
  }



  render() {
    return(
      <div className="right_convert">
        <div className="title">
          <h3>Dataset: </h3>
          {this.props.dataset}
        </div>
        <hr />
        { this.renderScreen(this.props.dataset) }
      </div>
    );
  }
}
export default Convert;
