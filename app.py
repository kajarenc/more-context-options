import streamlit as st

st.subheader("Headers")

st.write(st.context.headers)

st.write(f"Tornado returned :rainbow[IP Address]: {st.context.ip_address}")
