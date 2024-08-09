# mes importations
import streamlit as st
import pandas as pd

st.markdown("### Ceci est un titre énorme")

# un message de bienvenue
st.write("Bonjour DIT, comment allez vous ? Ici tout va bien par la grâce de Dieu")



# un dataframe
df = pd.DataFrame({
  'first column': [1, 2, 3, 4,5,6,7,8,9,10],
  'second column': [10, 20, 30, 40,50,60,70,80,90,100]
})

# affichage du dataframe
st.write(df)
