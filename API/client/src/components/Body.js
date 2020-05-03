import React, { useEffect, useState } from 'react';
import { browserHistory } from 'react-router';

const Body = () => {
  const [graph, setGraph] = useState();
  useEffect(() => {
    fetch("/graph")
    .then(res => res.json())
    .then(data => setGraph(data));
  })

    return (
      <div id="body">
      <h1>Sup {graph}</h1>
      </div>
    );
  }

export default Body;
