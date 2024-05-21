import streamlit as st

# Streamlit App
st.title("DAG Presales GH Klima Anlage ")

# Initialize session state for conversation history
if "history" not in st.session_state:
    st.session_state.history = []

# Text input for the user
user_input = st.text_input("You:", "")

if user_input:
    # Simulate a response (for now, we just echo the user input)
    response = f"Echo: {user_input}"
    # Append user input and response to the history
    st.session_state.history.append((user_input, response))

# Display conversation history
for user_text, bot_response in st.session_state.history:
    st.text_area("You:", value=user_text, height=50, max_chars=None, key=f"user_{user_text}")
    st.text_area("Chatbot:", value=bot_response, height=50, max_chars=None, key=f"bot_{bot_response}")

st.write("Type a message and press Enter to chat.")
