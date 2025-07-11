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
    user_input_lower = user_input.lower()

    # Tokenize user input into words
    user_words = set(user_input_lower.split())

    for _, row in df.iterrows():
        title_words = set(str(row["Title"]).lower().split())
        part_words = set(str(row["Part name"]).lower().split())

        # Check if any word in title or part name is in user input
        if user_words & title_words or user_words & part_words:
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

# If user submits a message
if submitted and user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get bot response and add to history
    response = get_response(user_input)
    st.session_state.messages.append({"role": "bot", "content": response})
