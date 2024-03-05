import streamlit as st
from htmlTemplate import css, bot_template, user_template
from utils.document_content_generator import get_api_response_content

def handle_userinput(user_question):
    print("hello")
    print(st.session_state.get('conversation', 0))
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)