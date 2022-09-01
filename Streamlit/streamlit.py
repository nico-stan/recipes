import streamlit as st


st.set_page_config(page_title="Recipe Generator", page_icon="🥗", layout='centered', initial_sidebar_state='auto')

st.markdown("<p align='center'>
            <img src='https://media1.giphy.com/media/39hvy4FM5au6JXeXOu/giphy.gif' />
            </p>")


st.markdown("<h1 style='text-align: center; color: white; font-size: +4'>Are you ready to start cooking?</h1>", unsafe_allow_html=True)
st.write("<h1 style='text-align: center; color: white; font-size: medium'>Let's get started!</h1>", unsafe_allow_html=True)            

#Check box for food restrictions
st.subheader("Food Restrictions")
    if st.checkbox("Do you have any food restrictions?"):
        restrictions_n = ["0","+1", "+2", "+3", "+4", "+5"]
        restrictions_line = st.radio(
            'How many food restrictions do you have?',
            restrictions)
        'You have selected: ', restrictions_line

        rest1 = 0 
        rest2 = 0 
        rest3 = 0 
        rest4 = 0 
        rest5 = 0
    

        if restrictions_line == "+1" or restrictions_line == "+2" or restrictions_line == "+3" or restrictions_line == "+4" or restrictions_line == "+5":
            rest1 = st.selectbox(
                'Seleccione your food restriction(s)',
                restrictions)
            'You have selected: ', rest1
            gr = st.slider('¿Cuál es la cantidad en gramos para este alimento de la cena?', 0, 500)
            p_gr= gr/100
            cen1 = pd.DataFrame(get.buscar_alimento_usuario(cena1))
            cen1 = funciones.alimentos_gr(cen1, p_gr)
            st.write(cen1)



        if linea_cena == "+2" or linea_cena == "+3" or linea_cena == "+4" or linea_cena == "+5":
            cena2 = st.selectbox(
            'Seleccione el segundo alimento para la cena',
            alimentos)
            'Has seleccionado: ', cena2
            gr = st.slider('¿Cuál es la cantidad en gramos para el segundo alimento de la cena?', 0, 500)
            p_gr= gr/100
            cen2 = pd.DataFrame(get.buscar_alimento_usuario(cena2))
            cen2 = funciones.alimentos_gr(cen2, p_gr)
            st.write(cen2)


        if linea_cena == "+3" or linea_cena == "+4" or linea_cena == "+5":
            cena3 = st.selectbox(
            'Seleccione el tercero alimento para la cena',
            alimentos)
            'Has seleccionado: ', cena3
            gr = st.slider('¿Cuál es la cantidad en gramos para el tercer alimento de la cena?', 0, 500)
            p_gr= gr/100
            cen3 = pd.DataFrame(get.buscar_alimento_usuario(cena3))
            cen3 = funciones.alimentos_gr(cen3, p_gr)
            st.write(cen3)

        if linea_cena == "+4" or linea_cena == "+5":
            cena4 = st.selectbox(
            'Seleccione el cuarto alimento para la cena',
            alimentos)
            'Has seleccionado: ', cena4
            gr = st.slider('¿Cuál es la cantidad en gramos para el cuarto alimento de la cena?', 0, 500)
            p_gr= gr/100
            cen4 = pd.DataFrame(get.buscar_alimento_usuario(cena4))
            cen4 = funciones.alimentos_gr(cen4, p_gr)
            st.write(cen4)

        if linea_cena == "+5":
            cena5 = st.selectbox(
            'Seleccione el quinto alimento para la cena',
            alimentos)
            'Has seleccionado: ', cena5
            gr = st.slider('¿Cuál es la cantidad en gramos para el quinto alimento de la cena?', 0, 500)
            p_gr= gr/100
            cen5 = pd.DataFrame(get.buscar_alimento_usuario(cena5))
            cen5 = funciones.alimentos_gr(cen5, p_gr)
            st.write(cen5)

        if linea_cena != "0":
            numero_cena = int(linea_cena[-1]) + 1
            cena_lista = [(globals()[f"cen{i}"]) for i in range(1,numero_cena)]
            cena = pd.concat(cena_lista[:numero_cena])
            st.write("Este es tu resumen del cena:", cena)

        if linea_cena != "0":
            suma_macros_cena = cena[["Energia(kcal)", "Grasas", "Proteina", "Carbohidratos"]].sum()
            st.write("Este es el total de tus macros para la cena", suma_macros_cena)

    param_area = "Food Restrictions"
    restrictions = ["None", "Dairy-free", "Gluten-free", "Nut-free", "Vegan", "Vegetarian" ]


#Check box for desired ingredients
st.subheader("Realfooder")
    if st.checkbox("Is there any ingredient you really want to include in your recipes?"):
        realfooder = ["0","+1", "+2", "+3", "+4", "+5"]
        realfooder_line = st.radio(
            'How many ingredients do you want to include in your recipes as must-haves?',
            realfooder)
        'You have selected: ', realfooder_line

        des1 = 0 
        des2 = 0 
        des3 = 0 
        des4 = 0 
        des5 = 0
        desayuno1 = 0 
        desayuno2 = 0 
        desayuno3 = 0 
        desayuno4 = 0 
        desayuno5 = 0

#Check box for undesired ingredients
st.subheader("Picky eater")
    if st.checkbox("Is there any ingredient you really want to exclude in your recipes?"):
        picky = ["0","+1", "+2", "+3", "+4", "+5"]
        picky_line = st.radio(
            'How many ingredients do you want to exclude in your recipes as must-haves?',
            picky)
        'You have selected: ', picky_line

        des1 = 0 
        des2 = 0 
        des3 = 0 
        des4 = 0 
        des5 = 0
        desayuno1 = 0 
        desayuno2 = 0 
        desayuno3 = 0 
        desayuno4 = 0 
        desayuno5 = 0




#select slider to choose time
time = st.slider('What is the maximum time (in min) you want to spend for a recipe?', min, max)

#select slider to choose n_steps
n_steps = st.slider('What is the maximum number of steps you want to have for a recipe?', min, max)

#select slider to choose n_recipes
n_recipes = st.slider('How many recipes do you want?', min, max)

st.write("You have selected:", time, "min", n_steps, "steps", n_recipes, "recipes")