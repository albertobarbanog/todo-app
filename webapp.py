import streamlit as st
import functions

def add_todo():


todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Enter a new todo", placeholder="e.g. Buy milk...",
              on_change=add_todo, key='new_todo')