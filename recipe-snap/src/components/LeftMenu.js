import React, { useState } from 'react';
import TextField from '@mui/material/TextField';


const LeftMenu = ({ onUrlSubmit }) => {
  const [url, setUrl] = useState('');

  const handleUrlChange = (event) => {
    setUrl(event.target.value);
  };

  const handleSubmit = () => {
    onUrlSubmit(url);
  };

  return (
    <div>
      <TextField
        label="Enter URL"
        variant="outlined"
        fullWidth
        value={url}
        onChange={handleUrlChange}
      />
      <button onClick={handleSubmit}>Submit</button>
    </div>
  );
};

export default LeftMenu;
