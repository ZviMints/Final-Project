
import React, { Component } from 'react';

export default class menu extends Component {    
    render() {
        return (
            <div className="menu">
            <div className="btn-group-vertical">
              <button type="button" className="btn btn-primary btn-lg active">Load</button> <br />
              <button type="button" className="btn btn-outline-primary mr-2">Convert</button> <br />
              <button type="button" className="btn btn-outline-primary mr-2">PCA</button> <br />
              <button type="button" className="btn btn-outline-primary mr-2">Results</button> <br />
            </div>
            </div>
          );
    }
}
