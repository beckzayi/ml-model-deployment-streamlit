import streamlit as st
import time
from PIL import Image

st.title('Machine Learning Model Deployment at the Server')

# header
st.header('Introduction')

# sub-heading
st.subheader('This is sub-header')

# text
st.text('This is text')

# input
input_text = st.text_input('Type something', 'default')
st.text(input_text)

input_text = st.text_area('Type something', 'default')