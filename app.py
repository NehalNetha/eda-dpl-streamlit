import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_csv("mental-health-students-streamlit.csv")

df.drop("Date", axis=1, inplace=True)

st.title('Mind Matters: Exploring the Relationship Between Mental Health and Academic Performance (CGPA) in College Students')

option1 = st.selectbox(
    'Select a graph to see occurance of values in columns?',
    ('Gender', 'Year of Study', "Anxiety", "Depression", "Panic Attack"))


st.bar_chart(df, x=  option1, y ="Age")







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


option_gpa= st.selectbox(
    'Select a graph to find Distributions?',
    ('CGPA vs Gender', 'CGPA vs Year of Study')
)


fig = px.histogram(df, x="CGPA", color="Gender",
                   marginal="box", # or violin, rug
                   hover_data=df.columns, title="Distribution of CGPA by Gender")

fig2= px.scatter(df, x="Year of Study", y="CGPA", color="Gender",
                   hover_data=df.columns, title="Distribution of CGPA by Year of Study")


if option_gpa == "CGPA vs Gender":

    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
elif option_gpa == "CGPA vs Year of Study":
    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)












option_box= st.selectbox(
    'Select a graph to find box plots?',
    ('CGPA vs Depression', 'CGPA vs Anxiety', "CGPA vs Depression vs Treatment", "CGPA vs Anxiety vs Treatment")
)

fig_box= px.box(df, x="Depression", y="CGPA",
                   hover_data=df.columns, title="CGPA vs Depression")


fig_box2= px.box(df, x="Anxiety", y="CGPA",
                   hover_data=df.columns, title="CGPA vs Depression")


fig_box3= px.box(df, x='Treatment', y='CGPA', color='Depression')

fig_box4= px.box(df, x='Treatment', y='CGPA',  color='Anxiety')








if option_box == "CGPA vs Depression":

    st.plotly_chart(fig_box, theme="streamlit", use_container_width=True)
elif option_box == "CGPA vs Anxiety":
    st.plotly_chart(fig_box2, theme="streamlit", use_container_width=True)

elif option_box == "CGPA vs Depression vs Treatment":
    st.plotly_chart(fig_box3, theme="streamlit", use_container_width=True)

elif option_box == "CGPA vs Anxiety vs Treatment":
    st.plotly_chart(fig_box4, theme="streamlit", use_container_width=True)

