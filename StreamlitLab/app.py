## import stramlit library
import streamlit as st

## Title
st.title('Streamlit Tutorial First App')

## Header
st.header('This is a header')

## Subheader
st.subheader('This is a subheader')

## body
st.text('Hello Streamlit')

## input
name = st.text_input('Enter your name', '')

## button
if st.button('Submit'):
    result = name.title()
    st.success(result)