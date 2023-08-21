import React from 'react';

const View = ({ response }) => {
  console.log(response)
  return (
    <div>
      <h2>Response:</h2>
      <p>{response.content}</p>
    </div>
  );
};

export default View;
