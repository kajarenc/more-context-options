import streamlit as st


st.write("URL")
st.write(st.context.url)


x = st.slider("Select a number", 0, 100, 50)
st.write(x**2)
