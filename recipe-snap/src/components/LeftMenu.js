import React, { useState } from 'react';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';

const LeftMenu = ({ onUrlSubmit }) => {
  const [url, setUrl] = useState('');

  const handleUrlChange = (event) => {
    setUrl(event.target.value);
  };

  const handleSample1Click = () => {
    setUrl('https://www.inspiredtaste.net/37475/homemade-chicken-noodle-soup-recipe/');
  };

  const handleSample2Click = () => {
    setUrl('https://www.inspiredtaste.net/41722/roasted-fingerling-potatoes/');
  };
  const handleSample3Click = () => {
    setUrl('https://www.inspiredtaste.net/18596/soft-and-chewy-oatmeal-raisin-cookie-recipe/');
  };

  const handleSubmit = () => {
    if (url !== '') {
      onUrlSubmit(url);
    }
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
      <Button variant="contained" onClick={handleSample1Click} style={{ marginRight: '8px', marginTop: '10px' }}>
        Sample 1
      </Button>
      <Button variant="contained" onClick={handleSample2Click} style={{ marginRight: '8px', marginTop: '10px' }}>
        Sample 2
      </Button>
      <Button variant="contained" onClick={handleSample3Click} style={{ marginRight: '8px', marginTop: '10px' }}>
        Sample 3
      </Button>
      <Button variant="contained" color="error" onClick={handleSubmit} style={{ marginRight: '8px', marginTop: '10px' }}>
        Submit
      </Button>
    </div>
  );
};

export default LeftMenu;
