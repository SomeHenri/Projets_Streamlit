# Programme pour le remplissage d4une base de données "SQLite"

# Importation des pacquages
import streamlit as st
import sqlite3

# je demande à la bibliothèque sqlite de me donner une connection
# sur ma base de données
conn = sqlite3.connect('students.db')

# ensuite je demande un curseur
# c'est grâce au curseur que je peux effectuer des requêtes
c = conn.cursor()

# la premire requete: je m'assure que la table existe, autrement je la crée
c.execute('''CREATE TABLE IF NOT EXISTS students
             (name TEXT, age INTEGER, major TEXT)''')
conn.commit()


# Navigation
# je veux un menu dans la marge
st.sidebar.title("Menu")

# je veux un bouton radio dans la marge afin de selectionner la page que je veux
page = st.sidebar.radio("Go to", ["List Students", "Add Student"])


# List Students Page
if page == "List Students":
    # j'affiche la liste des étudiants
    st.title("List of Students")
    st.write("Here you can see the list of students.")

    # je selectionne tous les étudiants depuis la table
    c.execute("SELECT * FROM students")
    # pour dire au système que vous voulez "posséder" les résultats de la requête
    # alors, il faut appeler la méthode fetchall
    students = c.fetchall()

    # je parcours mon objet student
    for student in students:
        # et j'affiche
        st.write(f"Name: {student[0]}, Age: {student[1]}, Major: {student[2]}")

# Add Student Page
elif page == "Add Student":
    st.title("Add a New Student")
    st.write("Enter student details below:")

    # formulaire d'ajout
    with st.form(key='add_student_form'):
        # les champs de mon formulaire
        name = st.text_input(label='Name')
        age = st.number_input(label='Age', min_value=1, max_value=100)
        major = st.text_input(label='Major')
        submit = st.form_submit_button(label='Add Student')

        # après soumission
        if submit:
            # j'insère en utilisant une requête SQL d'insertion
            c.execute("INSERT INTO students (name, age, major) VALUES (?, ?, ?)",
                      (name, age, major))

            # demander un enregistrement effectif de toutes les modifications effectuées
            conn.commit()
            # afficher un message de succès
            st.success(f"Added {name} to the database!")

conn.close()
