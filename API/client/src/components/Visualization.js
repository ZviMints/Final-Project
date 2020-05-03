import React, {useEffect, useState } from 'react';

import { Graph } from './Graph'
import Algorithms from './Algorithms'
import Menu from './Menu'

const Visualization = () => {

      const [graph, setGraph] = useState();

      useEffect(() => {
        fetch("/graph")
        .then(res => res.json())
        .then(data => setGraph(data));
      })

        return (
          <div id="visualization">
              <div className="row">
                <div className="menu_column">
                  <Algorithms />
                  <Menu />
                </div>

                <div className="graph_column">
                  <Graph graph={graph} />
                </div>
              </div>
          </div>
        );
}

export default Visualization;
