import streamlit as st
import pandas as pd

### streamlit run c:/Users/karim/OneDrive/Documents/Python/webapp/app.py

st.title("Topic Modeling to determine climate anxiety among youth")

st.header("Our mission and plan", divider='red')

st.markdown("We're using BERTopic and LDA as a baseline model")

page = st.selectbox('Select a page', ['modeling', 'LDA'])

import streamlit as st

# Create a dropdown in the sidebar for selecting page categories
category = st.sidebar.selectbox('Choose a category', ['General Info', 'Contact Info'])

# Display pages based on selected category
if category == 'General Info':
    page = st.sidebar.selectbox('Select a page', ['1_sentiment_analysis'])
    if page == '1_sentiment_analysis':
        st.write('1_sentiment_analysis')
        # Add content specific to the Home page


elif category == 'Contact Info':
    page = st.sidebar.selectbox('Select a page', ['2_modeling', '3_LDA'])
    if page == '2_modeling':
        st.write('2_modeling:')
        # Add content specific to the Contact page
    elif page == '3_LDA':
        st.write('3_LDA!')
        # Add content specific to the About page
