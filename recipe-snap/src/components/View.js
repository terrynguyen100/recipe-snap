import React from 'react';
import { List, ListItem, ListItemText, Typography } from '@mui/material';

const View = ({ response }) => {
  console.log(response);

  let ingredientList = null;
  let instructionList = null;

  if (response !== '') {
    ingredientList = response.ingredients.map((ingredient, index) => (
      <ListItem key={index}>
        <ListItemText primary={ingredient} />
      </ListItem>
    ));

    instructionList = response.instructions.map((instruction, index) => (
      <ListItem key={index}>
        <ListItemText primary={instruction} />
      </ListItem>
    ));
  }
  return (
    <div>
      {ingredientList && (
        <div>
          <Typography variant="h4">Ingredients:</Typography>
          <List>{ingredientList}</List>
        </div>
      )}
      {instructionList && (
        <div>
          <Typography variant="h4">Instructions:</Typography>
          <List>{instructionList}</List>
        </div>
      )}
    </div>
  );
};

export default View;
