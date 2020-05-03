import ReactDOM from 'react-dom'
import React, { Component } from 'react';
import './style.css'

import Header from './components/Header'
import Body from './components/Body'
import Footer from './components/Footer'

class Layout extends Component {
    render() {
        return (
            <div>
              <Header />
              <Body />
              <Footer />
            </div>
          );
    }
}

ReactDOM.render( <Layout />, document.querySelector("#root"));
