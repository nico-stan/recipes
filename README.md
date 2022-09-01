# Final Project - Recipe Generator

By: Nicolas Stambolsky

Date: September, 2nd 2022
<p align="center">
<img src="https://media1.giphy.com/media/39hvy4FM5au6JXeXOu/giphy.gif"
</p>  

________________________________________________

## Summary
Have you ever felt like cooking but not had the creativity to come up with unique recipes? Then this tool is meant for you. The aim of this project is to select a few custom parameters from a recipe database and generate the recipes for the user, as well as the shopping list so that you can cook without coming up with the recipes. 

## Methodology
I have selected a recipes dataset from [Kaggle](https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions) that was scrapped from [food.com](https://www.food.com/) of recipes gathered in English mostly in the US.

This dataset included over 200,000 recipes of different kind of foods. I selected only main dishes and created new columns to better filter by user preferences. This leads to a clean dataset `recipes.csv` to work with.

With this dataset I wanted to create the following tweaks:
- Filter by one or more food restrictions: Dairy-Free, Gluten-Free, Nut-Free, Vegan, Vegetarian
- Desired ingredients as a 'must have': Text from the user which must be in the dataset ingredients list.
- Undesired ingredients as a 'must not have': Text from the user.
- Filter by maximum cooking time: (e.g. 30 min or less).
- Filter by maximum number of steps (e.g. n_steps <= 5)
- Select how many recipes the user wants: (e.g. 10)

This project was initially developed in the queries jupyter notebook and most of its functions have been added to a Streamlit link which is still a work in progress. Therefore, there are some limitations to the project which are described in the Limitations and Further Development section of this file.


## Results
The public (work in progress) version of this tool can be found through this link in [Streamlit](https://nico-stan-recipes-streamlitstreamlit-rv1vwn.streamlitapp.com/) 

Here is what the results look like through the local version of this page:
![Local (working) version](https://github.com/nico-stan/recipes/blob/main/images/1.png)

![Local (working) version](https://github.com/nico-stan/recipes/blob/main/images/2.png)

In addition to this, there was a mapping function integrated in the jupyter notebook which allows the user to see the nearest Grocery Stores, within a 10 km radius grouped by walking distance up to 3km. This way, the user gets the recipes that they need, the shop list to buy the ingredients and the nearest Grocery Stores in the area.

![Map](https://github.com/nico-stan/recipes/blob/main/images/Map.png)

Furthermore, two graphs were developed to show the whole funnel process that depicts how many recipes are 'lost' in the way. 
![](https://github.com/nico-stan/recipes/blob/main/images/Pipeline.png)

And one that shows how restrictive each food restriction is, by showing the total amount of recipes available.
![](https://github.com/nico-stan/recipes/blob/main/images/Restrictions.png)

## Limitations
Notice that there were many hurdles during the development of this tool, some of which are explained in the EDA notebook. However, there are some issues that still remain to date, the main one regarding the inability to upload of the recipes.csv due to size which hampers the ability to use this tool if not run locally. Also, there are some technical problems regarding the Realfooder and Picky Eater functions in Streamlit, which would allow to select the desired/undesired ingredients from the dataset, even if it works perfectly fine in the `queries.ipynb`.

## Further Development
There are multiple ways in which this project can be expanded upon, which include but are not limited to:
- Solving the max size upload restriction on Github to run Streamlit not locally.
- Fixing minor details of the Realfooder and Picky Eater functions in `streamlit.py`
- Include more food restrictions as keto-diet, low-carb, Duncan, etc.
- Quantity scraping from [food.com](https://www.food.com/) to include a new column in the dataframe with quantities.
- Price and quantity Scraping from local stores to estimate the cart price based on the ingredients list.
- Save the queries, so that a prediction can be determined based on User Preferences after a couple of searches.
- Both translate the dataset and complement it with local foods so that the user can select available recipes based on location and not just heavily US-based recipes.
