import React, {useEffect, useState } from 'react';

import Graph from './Graph'
import Algorithms from './Algorithms'
import Menu from './Menu'

const Visualization = () => {

  const [graph_path, setGraphPath] = useState();

  const [algorithms, updateList] = useState([]);
  const remoteItem = (name) => {
    updateList(algorithms.filter(algorithm => algorithm !== name));
  };

      useEffect(() => {

      // POST request using fetch inside useEffect React hook
      const requestOptions = {
               method: 'POST',
               headers: { 'Content-Type': 'application/json' },
               body: JSON.stringify({ algorithms: "kmeans" })
      };

      fetch("/graph", requestOptions)
                .then(res => res.json())
                .then(data => setGraphPath(data));
      })

        return (
          <div id="visualization">
              <div className="row">
                <div className="menu_column">
                  <Algorithms algorithms={algorithms} updateList={updateList} remoteItem={remoteItem} />
                  <Menu />
                </div>

                <div className="graph_column">
                  <Graph algorithms={algorithms} graph_path={graph_path} />
                </div>
              </div>
          </div>
        );
}
export default Visualization;
