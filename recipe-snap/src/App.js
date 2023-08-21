import React, { useState } from 'react';
import './App.css';
import LeftMenu from './components/LeftMenu';
import View from './components/View';
import axios from 'axios';

function App() {
  const [response, setResponse] = useState('');

  const handleUrlSubmit = (url) => {
    axios.get(`/get_recipe?url=${url}`)
      .then((response) => {
        setResponse(response.data);
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
      })
  };

  return (
    <div className="App">
      <div className="left-menu">
        <LeftMenu onUrlSubmit={handleUrlSubmit} />
      </div>
      <div className="view">
        <View response={response} />
      </div>
    </div>
  );
}

export default App;
