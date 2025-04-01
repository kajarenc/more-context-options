import streamlit as st
import time

st.title("Page 1")

st.write("URL")
st.write(st.context.url)

x = st.slider("Select a number", 0, 100, 50)
st.write(x**2)


time.sleep(3)
