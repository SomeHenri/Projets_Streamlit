import streamlit as st

with st.form("MON FORMULAIRE"):
    st.write("Somme de 3 nombres")
     
    nb1 = st.number.input("Nombre 1")
    nb2 = st.number.input("Nombre 2")
    nb3 = st.number.input("Nombre 3")
    
    submitted = st.form_submit_button("Soumettre")
    
    if submitted:
        st.write("La somme des trois nombres est:", nb1 + nb2 + nb3)
        
st.write("MERCI")

