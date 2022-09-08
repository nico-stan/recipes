import ast                     # Change lists that are strings to actual lists
import numpy as np             # Generate empty lists
import pandas as pd            # Read the csv as df
import warnings                # Makes it readable without 'errors'
warnings.filterwarnings("ignore")
from src.recipes import * #Functions to filter the df
import streamlit as st # Create and populate a website
import inflect
p = inflect.engine()

st.set_page_config(page_title="Recipe Generator", page_icon="🥗", layout='centered', initial_sidebar_state='auto')

# Centering the desired GIF
col1, col2, col3 = st.columns([1,6,1])
with col1:
    st.write("")
with col2:
    st.image("https://media1.giphy.com/media/39hvy4FM5au6JXeXOu/giphy.gif")
with col3:
    st.write("")

# Title and subtitle
st.markdown("<h1 style='text-align: center; color: white; font-size: +4'>Are you ready to start cooking?</h1>", unsafe_allow_html=True)
st.write("<h1 style='text-align: center; color: white; font-size: large'>Let's get started!</h1>", unsafe_allow_html=True)            

# importing the df
df = pd.read_pickle('https://raw.githubusercontent.com/nico-stan/recipes/main/data/recipes.csv.pkl')
df.drop(columns='id', inplace=True)
df.nutrition.apply(nutrition_values)


# Check box for food restrictions
st.subheader("Food Restrictions")
if st.checkbox("Do you have any food restrictions?"):
    restrictions =  []
    if st.checkbox('Dairy-free'):
        restrictions.append('dairy')
    if st.checkbox('Gluten-free'):
        restrictions.append('gluten')
    if st.checkbox('Nut-free'):
        restrictions.append('nuts')
    if st.checkbox('Vegetarian'):
        restrictions.append('non-veggie')
    if st.checkbox('Vegan'):
        restrictions.append('non-vegan')
    df2 = restrict(df, *restrictions)
else:
    df2  = restrict(df)

# Check box for desired ingredients
st.subheader("Realfooder")
#ing_list=[]
#for row in df.ingredients:
#    ing_list+=row
#ing_list = set(ing_list)
if st.checkbox("Is there any ingredient you really want to include in your recipes?"):
    realfooder = [1, 2, 3]
    realfooder_line = st.radio(
        'How many ingredients do you want to include in your recipes as must-haves?',
        realfooder)     
#    if realfooder_line == 1:
#        ing = st.text_input("Enter the name of the ingredient")
#        df3 = realfooder(df2, ing_list, ing)
#    elif realfooder_line == 2:
#        ing1 = st.text_input("Enter the name of the 1st ingredient")
#        ing2 = st.text_input("Enter the name of the 2nd ingredient")       
#        df3 = realfooder(df2, ing_list, ing1, ing2)
#    elif realfooder_line == 3:
#        ing1 = st.text_input("Enter the name of the 1st ingredient")
#        ing2 = st.text_input("Enter the name of the 2nd ingredient")
#        ing3 = st.text_input("Enter the name of the 3rd ingredient")     
#        df3 = realfooder(df2, ing_list, ing1, ing2, ing3)
#else:
#    df3 = realfooder(df2, ing_list)


# Check box for undesired ingredients
st.subheader("Picky eater")
if st.checkbox("Is there any ingredient you really want to exclude in your recipes?"):
    picky = [1, 2, 3]
    picky_line = st.radio(
        'How many ingredients do you want to exclude in your recipes as must-haves?',
        picky)

# Drag slider to select time, n_steps, n_recipes
st.subheader("Time management")
t_max = st.slider('What is the maximum time (in min) you want to spend for a recipe?', 200 , 0)
df3 = df2[df2.minutes <= t_max].reset_index(drop=True)
n_steps = st.slider('What is the maximum number of steps you want to have for a recipe?', 30, 0)
df4 = df3[df3.n_steps <= n_steps].reset_index(drop=True)
n_recipes = st.slider('How many recipes do you want?', 1, 30)
pick = n_of_recipes(len(df4), n_recipes)
pick = [n-1 for n in pick]

st.write("You have selected: ", n_recipes, "recipes with a max cooking time of ", t_max, "min and a max amount of ", n_steps, "steps")


# Show the df final and shop_list

st.subheader("Recipes and Shop List")
df_chosen = df4.filter(items = pick, axis=0).reset_index(drop=True)
df_final = df_chosen[['name','description', 'minutes', 'ingredients', 'steps', 'restrictions', 'url' ]]
st.write("Here are your recipes:")
st.write(df_final)

shop_list=[]
for row in df_chosen.ingredients:
    shop_list+=row
shop_list = list(set(shop_list))
shop_list.sort()

words=[]
shop_list_def = []
for item in shop_list:
    for word in item.split(' '):
        if p.singular_noun(word):
            word = p.singular_noun(word)
        if word not in words:
            words.append(word)
            shop_list_def.append(item)
shop_list_def = list(set(shop_list_def))
shop_list_def.sort()
st.write("Here is your shopping list with ", len(shop_list_def), "items:")
st.write(shop_list_def)
if st.checkbox("Do you already have any of the mentioned ingredients?"):
    stock = st.selectbox('Seleccione alimento:', shop_list_def)
    shop_list_def.remove(stock)
    st.write("You have removed ", stock, "from the shopping list")
    st.write("Here is your updated shopping list with ", len(shop_list_def), "items:")
    st.write(shop_list_def)


# graph the pipeline 231637 and diets
# link1 = "https://github.com/nico-stan/recipes/blob/main/images/Pipeline.png"
# st.image(link1, caption= 'Recipe Pipeline', width=350)

# link2 = "https://github.com/nico-stan/recipes/blob/main/images/Restrictions.png"
# st.image(link2, caption= '# Recipes by Restriction', width=350)

# Show the map with the nearest grocery stores to buy the shop_list
# link3 = "https://github.com/nico-stan/recipes/blob/main/images/Map.png"
# st.image(link3, caption= '# Recipes by Restriction', width=350)