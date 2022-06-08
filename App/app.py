import streamlit as st
from multiapp import MultiApp
from apps import home, about # import your app modules here

app = MultiApp()

st.markdown("""
# Emotion Detection Using Text
""")

# Add all your application here
app.add_app("About", about.app)
app.add_app("Home", home.app)

# The main app
app.run()