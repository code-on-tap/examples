import React from 'react';
import './App.css';

import Red from './components/red'

function App() {
  return (
    <div className="App" style={{ backgroundColor: '#ccc' }}>
      <div>
        <p>Edit <code>src/App.js</code> and save to reload.</p>
        <a className="App-link" href="https://reactjs.org" target="_blank" rel="noopener noreferrer">Learn React</a>
      </div>

      <Red />
    </div>
  );
}

export default App;
