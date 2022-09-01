# Final Project - Recipe Generator

By: Nicolas Stambolsky

Date: September, 2nd 2022

![Screenshot](https://media1.giphy.com/media/39hvy4FM5au6JXeXOu/giphy.gif)
________________________________________________

## Summary
Have you ever felt like cooking but not had the creativity to come up with unique recipes? Then this tool is meant for you. The idea is to select a few custom parameters from a recipe database and generate the recipes for you, as well as the shopping list so that you can cook without coming up with the recipes. 

## Methodology
I have selected a recipes dataset from [Kaggle](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions) that was scrapped from [food.com](https://www.food.com/) of recipes gathered in English mostly in the US.

This dataset included over 200,000 recipes of different kind of foods. I selected only main dishes and created new columns to better filter by user preferences. This lead to a clean dataset 'recipes.csv' to work with.

With this dataset I wanted to create the following tweaks:
- Filter by one or more food restrictions: Dairy-Free, Gluten-Free, Nut-Free, Vegan, Vegetarian
- Desired ingredients as a 'must have': Text from the user which must be in the dataset ingredients list.
- Undesired ingredients as a 'must not have': Text from the user.
- Filter by maximum cooking time: (e.g. 30 min or less).
- Filter by maximum number of steps (e.g. n_steps <= 5)
- Select how many recipes the user wants: (e.g. 10)

This project was initially developed in the queries jupyter notebook and most of its functions have been added to a Streamlit link which is still a work in progress.


## Results


Once this selection is done, 
