import streamlit as st
import pandas as pd

# Load the Excel data
df = pd.read_excel("List.xlsx")

# Title of the app
st.title("3D Printer requirement Chatbot Demo")

# User input
user_input = st.text_input("Ask me about a 3D printer part or function for which you would like to know the requirements:")

def get_response(user_input):
    for _, row in df.iterrows():
        title = row["Title"].lower()
        part_name = row["Part name"].lower()
        if title in user_input.lower() or part_name in user_input.lower():
            return row["Description"]
    return ("Sorry, I couldn't find any specification for that part. "
            "Which part of the 3D printer are you interested in?")

# Respond when user submits input
if user_input:
    response = get_response(user_input)
    st.write("💬 " + response)