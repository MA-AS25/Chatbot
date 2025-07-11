import streamlit as st
import pandas as pd

# Load the Excel data
df = pd.read_excel("List.xlsx")

# Title of the app
st.title("3D Printer requirement Chatbot Demo")
st.write("Ask me about a 3D printer part or function for which you would like to know the requirements:")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to get response from Excel
def get_response(user_input):
    for _, row in df.iterrows():
        title = row["Title"].lower()
        part_name = row["Part name"].lower()
        if title in user_input.lower() or part_name in user_input.lower():
            return row["Description"]
    return ("Sorry, I couldn't find any specification for that part. "
            "Which part of the 3D printer are you interested in?")

# Display chat messages from history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    else:
        st.markdown(f"**Bot:** {message['content']}")
        
# Chat input using a form (to avoid rerun conflicts)
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Type your message here:")
    submitted = st.form_submit_button("Send")

# When user submits a message
if submitted and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = get_response(user_input)
    st.session_state.messages.append({"role": "bot", "content": response})
