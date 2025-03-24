import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("vehicles_us.csv")

# Data Cleaning and Handling Missing Values
# Fill is_4wd missing values with 0 and convert to bool
df['is_4wd'] = df['is_4wd'].fillna(0).astype(bool)

# Fill paint_color missing values with 'unknown'
df['paint_color'] = df['paint_color'].fillna('unknown')

# Fill cylinders based on median per vehicle type
df['cylinders'] = df[['cylinders', 'type']].groupby('type').transform(lambda x: x.fillna(x.median()))

# Fill model_year based on median per model
df['model_year'] = df[['model_year', 'model']].groupby('model').transform(lambda x: x.fillna(x.median()))

# Fill odometer based on median per model
df['odometer'] = df[['odometer', 'model']].groupby('model').transform(lambda x: x.fillna(x.median()))

# Streamlit App
st.title("Used Cars Data Analysis Dashboard")

st.write("Explore the dataset of used car advertisements.")

# Sidebar Filters
st.sidebar.header("Filters")

car_types = ["All"] + sorted(df["type"].unique().tolist())
selected_type = st.sidebar.selectbox("Select Car Type:", car_types)

min_price, max_price = int(df["price"].min()), int(df["price"].max())
price_range = st.sidebar.slider("Price Range ($):", min_price, max_price, (min_price, max_price))

# Apply filters
filtered_data = df.copy()
if selected_type != "All":
    filtered_data = filtered_data[filtered_data["type"] == selected_type]

filtered_data = filtered_data[(filtered_data["price"] >= price_range[0]) & (filtered_data["price"] <= price_range[1])]

# Display filtered dataset size
st.write(f"Number of vehicles after filters: {len(filtered_data)}")

# Histogram for car price distribution
st.header("Price Distribution")
fig_price_hist = px.histogram(filtered_data, x="price", nbins=50, title="Price Distribution of Used Cars")
st.plotly_chart(fig_price_hist)

# Scatter plot for price vs odometer
st.header("Price vs. Odometer")
fig_scatter = px.scatter(filtered_data, x="odometer", y="price", color="type", title="Price vs. Odometer by Car Type")
st.plotly_chart(fig_scatter)

# Pie chart for vehicle types
st.header("Distribution by Car Type")
fig_pie = px.pie(filtered_data, names="type", title="Distribution of Vehicles by Type")
st.plotly_chart(fig_pie)

# Checkbox to show data table
if st.checkbox("Show Data Table"):
    st.write(filtered_data.head(50))

st.write("\n")
st.write("Created by Mikhail as part of a TripleTen learning project.")
