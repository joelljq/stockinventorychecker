import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv("Store Inventory Dataset.csv")

st.title("Store Inventory")

st.subheader('Full Inventory Table')
st.dataframe(df)

def update_value(df, index, column, new_value):
    """
    Update a value in the DataFrame at a specific row index and column
    """
    df.at[index, column] = new_value
    return df

value = st.text_input("Enter a item name: ")

if value:
    filtered_df = df[df['Item Name'].str.contains(value, case=True, na=False, regex=False)]
    st.subheader(f"Search Results for '{value}'")
    st.dataframe(filtered_df)

    if not filtered_df.empty:

        indextoedit = st.selectbox("Select row index to edit: ", filtered_df.index)

        columntoedit = st.selectbox("Select column to edit: ", df.columns)

        new_value = st.text_input("Enter new value: ")

        if st.button("Update"):
            df = update_value(df, indextoedit, columntoedit, new_value)
            st.success(f"Updated row {indextoedit}, column '{columntoedit}' to '{new_value}'")
            st.dataframe(df)
else:
    st.write("Error not found")