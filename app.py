# Save this in the same folder as books.csv
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

# Load Data
df = pd.read_csv('books.csv')

# Preprocessing
rating_map = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
df['Rating_Num'] = df['Rating'].map(rating_map)
df['Price_Num'] = df['Price'].str.replace('£', '').astype(float)

# Sidebar
st.sidebar.title("📊 Filter")
min_rating = st.sidebar.slider("Minimum Rating", 1, 5, 1)
filtered_df = df[df['Rating_Num'] >= min_rating]

# Title
st.title("📚 Book Price & Rating Dashboard")

# Show data
if st.checkbox("Show Raw Data"):
    st.write(filtered_df)

# Rating Count
st.subheader("⭐ Rating Count")
fig1, ax1 = plt.subplots()
sns.countplot(x='Rating_Num', data=filtered_df, ax=ax1, palette='pastel')
st.pyplot(fig1)

# Price Distribution
st.subheader("💰 Price Distribution")
fig2, ax2 = plt.subplots()
sns.histplot(filtered_df['Price_Num'], bins=10, kde=True, ax=ax2, color='skyblue')
st.pyplot(fig2)

# Price vs Rating
st.subheader("📈 Price vs Rating")
fig3, ax3 = plt.subplots()
sns.scatterplot(x='Rating_Num', y='Price_Num', data=filtered_df, ax=ax3)
st.pyplot(fig3)

# Top Expensive & Cheap
st.subheader("💎 Top 5 Most Expensive Books")
st.write(filtered_df.sort_values(by='Price_Num', ascending=False).head(5))

st.subheader("💸 Top 5 Cheapest Books")
st.write(filtered_df.sort_values(by='Price_Num').head(5))
