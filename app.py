import streamlit as st
import pandas as pd
import plotly.express as px
import ipywidgets as widgets
from IPython.display import display
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("vehicles_us.csv")

# Header
st.header("Used Cars Data Dashboard")

# Show dataframe with checkbox
if st.checkbox("Show Raw Data"):
    st.write(df.head())

# Histogram of price
st.subheader("Price Distribution")
st.plotly_chart(px.histogram(df, x="price", nbins=50, title="Price Distribution of Cars"))

# Scatter plot: price vs odometer
st.subheader("Price vs Odometer")
st.plotly_chart(px.scatter(df, x="odometer", y="price", color="type", title="Price vs Odometer Reading"))

# Pie chart of car conditions
st.subheader("Condition Distribution")
condition_counts = df["condition"].value_counts().reset_index()
condition_counts.columns = ["condition", "count"]
fig_pie = px.pie(condition_counts, names="condition", values="count", title="Car Condition Distribution")
st.plotly_chart(fig_pie)

# Box plot: price by transmission
st.subheader("Price by Transmission Type")
st.plotly_chart(px.box(df, x="transmission", y="price", title="Price Variation by Transmission"))

# Add interactive slider for model year
st.subheader("Price Distribution for Selected Model Year")
year = st.slider("Select model year:", int(df["model_year"].min()), int(df["model_year"].max()), 2015)
st.plotly_chart(px.histogram(df[df["model_year"] == year], x="price", nbins=50, title=f"Price Distribution for Model Year {year}"))
