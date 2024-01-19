import streamlit as st
import numpy as np


st.set_page_config(
    page_title="ChatBot",
    page_icon="👋",
)

st.write("# Welcome to My ChatBot")

prompt = st.chat_input("Say something")

if 'data' not in st.session_state:
    st.session_state.data  = []

if prompt:
    st.session_state.data.append(prompt)
    for text in st.session_state.data:
        st.write(f"User has sent the following prompt: {text}")

st.write(st.session_state.data)


message = st.chat_message("assistant")
message.write("Hello human")
message.bar_chart(np.random.randn(30, 3))

message1 = st.chat_message("user")
message1.write("Thanks")

col1, col2, col3 = st.columns(3)



# col1.header("aaaaa")

with col1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")

with st.expander("See explanation"):
    st.write("The chart above shows some numbers I picked for you. I rolled actual dice for these, so they're guaranteed to be random.")
    st.image("https://static.streamlit.io/examples/dice.jpg")   

# st.sidebar.success("Select a demo above.")
