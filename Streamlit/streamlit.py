
import streamlit as st # Create and populate a website

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


# Check box for desired ingredients
st.subheader("Realfooder")
if st.checkbox("Is there any ingredient you really want to include in your recipes?"):
    realfooder = [1, 2, 3]
    realfooder_line = st.radio(
        'How many ingredients do you want to include in your recipes as must-haves?',
        realfooder)
     
#    if realfooder_line == 1:
#        ing = st.text_input("Enter the name of the ingredient")
#        df3 = realfooder(df, ing_list, ing)
#    elif realfooder_line == 2:
#        ing1 = st.text_input("Enter the name of the 1st ingredient")
#        ing2 = st.text_input("Enter the name of the 2nd ingredient")       
#        df3 = realfooder(df, ing_list, ing1, ing2)
#    elif realfooder_line == 3:
#        ing1 = st.text_input("Enter the name of the 1st ingredient")
#        ing2 = st.text_input("Enter the name of the 2nd ingredient")
#        ing3 = st.text_input("Enter the name of the 3rd ingredient")     
#        df3 = realfooder(df, ing_list, ing1, ing2, ing3)
# else:
#    df3 = realfooder(df, ing_list)


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

n_steps = st.slider('What is the maximum number of steps you want to have for a recipe?', 30, 0)

n_recipes = st.slider('How many recipes do you want?', 30, 0)

st.subheader("Results")
st.write("You have selected: ", n_recipes, "recipes with a max cooking time of ", t_max, "min and a max amount of ", n_steps, "steps")
