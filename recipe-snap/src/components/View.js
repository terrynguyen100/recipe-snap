import React from 'react';
import { List, ListItem, ListItemText, Typography } from '@mui/material';

const View = ({ response }) => {
  let ingredientList = [];
  let instructionList = [];

  if (response.ingredients) {
    ingredientList = response.ingredients.map((ingredient, index) => (
      <ListItem key={index}>
        <ListItemText primary={ingredient} />
      </ListItem>
    ));
  }

  if (response.instructions) {
    instructionList = response.instructions.map((instruction, index) => (
      <ListItem key={index}>
        <ListItemText primary={instruction} />
      </ListItem>
    ));
  }

  return (
    <div>
      {ingredientList.length > 0 && (
        <div>
          <Typography variant="h4">Ingredients:</Typography>
          <List>{ingredientList}</List>
        </div>
      )}
      {instructionList.length > 0 && (
        <div>
          <Typography variant="h4">Instructions:</Typography>
          <List>{instructionList}</List>
        </div>
      )}
      {instructionList.length === 0 && ingredientList.length === 0 && (
        <Typography variant="h4" color="error">No data found for this URL</Typography>
      )}

    </div>
  );
};

export default View;
