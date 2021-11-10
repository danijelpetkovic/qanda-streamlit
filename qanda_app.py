import streamlit as st
import pandas as pd
import numpy as np

st.title('Ask an interesting question')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data = load_data(10000)



st.text_input('Enter a question')

st.checkbox('Enable voice')

confirm_button = st.button('Get an answer')

def main():
    if confirm_button:
        st.spinner("Generating an answer...")

st.text('This is an answer')

main()