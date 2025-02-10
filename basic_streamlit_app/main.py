import streamlit as st
import pandas as pd

# display a title
st.title('Streamlit Basic App')

# describe the app
st.write("This is a basic Streamlit app that loads a sample dataset and allows interactive filtering")

# load a CSV file
df = pd.read_csv('basic_streamlit_app/data/penguins.csv')


# display the imported dataset
st.write("Here is the dataset loaded from a CSV file:")
st.dataframe(df)

# Using a selectbox to filter data by species
species = st.selectbox("Select a species", df['species'].unique())
filtered_df = df[df['species'] == species]

# Display the filtered results
st.write(f"Penguin {species}:")
st.dataframe(filtered_df)