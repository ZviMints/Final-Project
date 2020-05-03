import React, {useEffect, useState } from 'react';

import Graph from './Graph'
import Algorithms from './Algorithms'
import Menu from './Menu'

const Visualization = () => {

  const [graph, setGraph] = useState();

  const [algorithms, updateList] = useState([]);
  const remoteItem = (name) => {
    updateList(algorithms.filter(algorithm => algorithm !== name));
  };

      useEffect(() => {
        fetch("/graph")
        .then(res => res.json())
        .then(data => setGraph(data));
      })

        return (
          <div id="visualization">
              <div className="row">
                <div className="menu_column">
                  <Algorithms algorithms={algorithms} updateList={updateList} remoteItem={remoteItem} />
                  <Menu />
                </div>

                <div className="graph_column">
                  <Graph algorithms={algorithms} graph={graph} />
                </div>
              </div>
          </div>
        );
}
export default Visualization;
