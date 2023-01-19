#Import the required Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import matplotlib.patches as mpatches
import plotly_express as px
import plotly.figure_factory as ff
from sklearn.cluster import KMeans

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

def cluster_plot(x,y,kmeans,data_with_clusters):
    fig, ax = plt.subplots(1,1)
    plt.xticks(rotation=90)
    # plt.bar(df['Annual income'].value_counts().to_frame().index,df['Annual income'].value_counts().to_frame()['Annual income'])
    plt.title('Clusters')
    # plt.scatter(x[y==0,0],x[y==0,1],s=90,c='plum',label='Category 1')
    plt.scatter(data_with_clusters['Age'],data_with_clusters['Standard'],c=data_with_clusters['Clusters'],cmap='rainbow')
    plt.xlabel('Age')
    # plt.scatter(x[y==1,0],x[y==1,1],s=90,c='teal',label='Category 2')
    plt.ylabel('Standard')
    # plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=90,c='yellow',label='Centroids')
    plt.legend()

    st.pyplot(fig)

def ml():
    st.header('Categorisation of students into different clusters') 
    df['Area_of_interest_in_academics2']=df['Area of interest in academics']
    df2=df.assign(Area_of_interest_in_academics2=df.Area_of_interest_in_academics2.str.split(",")).explode('Area_of_interest_in_academics2').reset_index()
    df2.Area_of_interest_in_academics2=df2.Area_of_interest_in_academics2.apply(lambda x:x.strip())
    df['Area_of_interest_in_extra_curricular_activities2']=df['Area of interest in extra curricular activities']
    df2=df.assign(Area_of_interest_in_extra_curricular_activities2=df.Area_of_interest_in_extra_curricular_activities2.str.split(",")).explode('Area_of_interest_in_extra_curricular_activities2').reset_index()
    df2.Area_of_interest_in_extra_curricular_activities2=df2.Area_of_interest_in_extra_curricular_activities2.apply(lambda x:x.strip())
    df3=df2[['Age','Standard','Area of interest in academics','Area of interest in extra curricular activities']]
    df3_cat=df3[['Area of interest in academics','Area of interest in extra curricular activities']]
    df3_dummy=pd.get_dummies(df3_cat)
    df3=df3.drop(df3_cat,axis=1)
    df3=pd.concat([df3,df3_dummy],axis=1)

    x = df3.iloc[:,:].values

    kmeans=KMeans(n_clusters=2,init='k-means++',n_init=10,max_iter=300,random_state=0)
    y = kmeans.fit_predict(x)
    data_with_clusters = df3.copy()
    data_with_clusters['Clusters'] = y 
    st.write('Now data is being clustered into 2 clusters "cluster 0" and "cluster 1"')
    st.write('Header of data with cluter group = 0')
    st.write(data_with_clusters[data_with_clusters['Clusters']==0].head())
    st.write('Header of data with cluter group = 1')
    st.write(data_with_clusters[data_with_clusters['Clusters']==1].head())
    cluster_plot(x,y,kmeans,data_with_clusters)

    

# Add a title and intro text
st.title('Student Data Analysis')
st.text("Let's explore data")

# Sidebar setup
st.sidebar.title('Sidebar')
upload_file = st.sidebar.file_uploader('Upload a data')
#Sidebar navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select what you want to display:', ['Home', 'Data Summary', 'Data Header', 'Plots','Clusters'])


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
elif options == 'Clusters':
    ml()
