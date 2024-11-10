import streamlit as st
import pandas as pd
import pickle


def load_pickle_file(file_path='product.pkl'):
    with open(file_path, 'rb') as file:
        return pickle.load(file)


# Helper function to find similar products
def find_similar_products(product_name, df, num_results=10):
    df['similarity'] = df['product_name'].apply(lambda x: product_name.lower() in x.lower())
    similar_products = df[df['similarity']].head(num_results)
    return similar_products[['brand', 'product_name']]


# Streamlit App
st.title("Product Recommendation System")

# Load the dataset
try:
    df = load_pickle_file()  # Default file path to 'product.pkl'
    st.success("Data loaded successfully!")
    st.dataframe(df)  # Show first 5 rows of the data

    # Search for similar products
    product_name = st.text_input("Enter Product Name to Search:", "")
    if st.button("Find Similar Products"):
        if product_name:
            results = find_similar_products(product_name, df)
            if not results.empty:
                st.write(f"Top {len(results)} similar products:")
                st.dataframe(results)
            else:
                st.warning("No similar products found.")
        else:
            st.warning("Please enter a product name.")
except FileNotFoundError:
    st.error("The file 'product.pkl' was not found. Please make sure it's in the same directory as this script.")