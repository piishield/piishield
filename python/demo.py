import streamlit as st
import openai
import recognize

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')
openai.api_key = openai_api_key

st.title('PIIShield')


with st.form('my_form'):
    text = st.text_area('Enter text:', 'Hi, my name is Amy! My email is amy@work.com')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        st.info(recognize.redact_text(text))
