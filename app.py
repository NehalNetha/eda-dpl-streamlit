import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv("mental-health-students-streamlit.csv")

df.drop("Date", axis=1, inplace=True)

option1 = st.selectbox(
    'Select a graph to see occurance of values in columns?',
    ('Gender', 'Year of Study', "Anxiety", "Depression", "Panic Attack"))


st.bar_chart(df, x=  option1, y ="Age")





option = st.selectbox(
    'Select a graph?',
    ('Gender', 'Year of Study'))


st.bar_chart(df, x=  option, y ="Age")


option_rel= st.selectbox(
    'Select a graph to find relations?',
    ('Age vs Depression', 'Year of Study vs Depression', "Year of Study vs Anxiety","Year of Study vs Anxiety", "Age vs Anxiety"))


if option_rel == 'Age vs Depression':
    st.bar_chart(df, x=  "Age", color="Depression")
elif option_rel == 'Age vs Anxiety':
    st.bar_chart(df, x=  "Age", color="Anxiety")
elif option_rel == 'Year of Study vs Depression':
    st.bar_chart(df, x=  "Year of Study", color="Depression")
elif option_rel == 'Year of Study vs Anxiety':
    st.bar_chart(df, x=  "Year of Study", color="Anxiety")
elif option_rel == 'Year of Study vs Anxiety':
    st.bar_chart(df, x=  "Year of Study", color="Treatment")

    