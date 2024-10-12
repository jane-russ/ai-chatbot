import streamlit as st

st.title(":brain: Jane's Chatbot  🎈  ")
# Initialize session state for storing chat history 
if "chat_history" not in st.session_state: 
    st.session_state.chat_history = []  # Initialize with an empty list

# Display the user input 
#if user_input := st.text_input("You: ", placeholder="Type your message here..."): 
    #st.session_state.chat_history.append(user_input) 

# Display all messages using st.write 
for message in st.session_state.chat_history: 
    with st.chat_message("user"): 
        st.markdown(message) 
# Capture user input and append to chat history 
if prompt := st.chat_input("Type your message here ..."): 
    st.session_state.chat_history.append(prompt) 
    st.chat_message("user").markdown(prompt) 
