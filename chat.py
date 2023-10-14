import streamlit as st
import pprint
import google.generativeai as palm


palm.configure(api_key='AIzaSyCzKzS0Fnhk0o2eWWkdNzU0VZRzGAgug2s')
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
# Title of the app
st.title("Trying PALM")


# Chat container
chat_container = st.empty()

# User input
user_input = st.text_input("Enter your message:")

if st.button("Send"):
    completion=palm.generate_text(
        model=model,
        prompt=user_input,
        temperature=0,
        max_output_tokens=800,
    )
    chat_container.text(f"You: {completion.result}")

