#Import the required Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import matplotlib.patches as mpatches
import plotly_express as px
import plotly.figure_factory as ff

st.set_page_config(layout="wide")

# Functions for each of the pages
def home(uploaded_file):
    if uploaded_file:
        st.header('Begin exploring the data using the menu on the left')
    else:
        st.header('To begin please upload a file')

def data_summary():
    st.header('Statistics of Dataframe')
    st.write(df.describe())

def data_header():
    st.header('Header of Dataframe')
    st.write(df.head())

def displayplot():
    

    fig, ax = plt.subplots(1,1)
    plt.bar(df['Internet facility'].value_counts().to_frame().index,df['Internet facility'].value_counts().to_frame()['Internet facility'])
    plt.title('Internet facility')
    st.pyplot(fig)

    fig, ax = plt.subplots(1,1)
    plt.bar(df['Extra reading habit'].value_counts().to_frame().index,df['Extra reading habit'].value_counts().to_frame()['Extra reading habit'])
    plt.title('Extra reading habit')
    st.pyplot(fig)

    fig, ax = plt.subplots(1,1)
    plt.bar(df['Differently abled'].value_counts().to_frame().index,df['Differently abled'].value_counts().to_frame()['Differently abled'])
    plt.title('Differently abled')
    st.pyplot(fig)

    fig, ax = plt.subplots(1,1)
    plt.bar(df['Health issues'].value_counts().to_frame().index,df['Health issues'].value_counts().to_frame()['Health issues'])
    plt.title('Health issues')
    st.pyplot(fig)

    fig, ax = plt.subplots(1,1)
    plt.xticks(rotation=90)
    plt.bar(df['Annual income'].value_counts().to_frame().index,df['Annual income'].value_counts().to_frame()['Annual income'])
    plt.title('Annual income')
    st.pyplot(fig)


    

   


# Add a title and intro text
st.title('Student Data Analysis')
st.text("Let's explore data")

# Sidebar setup
st.sidebar.title('Sidebar')
upload_file = st.sidebar.file_uploader('Upload a data')
#Sidebar navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select what you want to display:', ['Home', 'Data Summary', 'Data Header', 'Plots'])


# Check if file has been uploaded
if upload_file is not None:
    df = pd.read_csv(upload_file)

# Navigation options
if options == 'Home':
    home(upload_file)
elif options == 'Data Summary':
    data_summary()
elif options == 'Data Header':
    data_header()
elif options == 'Plots':
    displayplot()

