# sd_tools_project
Sptint 6. Software Developmant Tools.
Vehicle Ads Dashboard

# Streamlit Dashboard Project Readme

## Project Overview
This project is an interactive dashboard built with **Streamlit**, showcasing data exploration and visualization.

It demonstrates how to:
- Load and analyze datasets with **pandas**.
- Visualize data using **plotly.express** and **altair**.
- Build interactive web applications with **Streamlit**.

## Features
- Interactive histograms and scatter plots for data analysis.
- Pie charts for visualizing categorical data.
- Widgets like checkboxes and sliders to adjust the output in real-time.

## Technologies Used
- Python 3
- pandas
- streamlit
- plotly.express
- altair

## Installation
1. Clone the repository:
```
git clone <your-repo-url>
```
2. Navigate to the project folder:
```
cd <your-project-folder>
```
3. (Optional) Create and activate a virtual environment.
4. Install the project requirements:
```
pip install -r requirements.txt
```
5. Launch the app:
```
streamlit run app.py
```

## Deployment Instructions
1. Ensure your repository contains the following files:
   - `app.py`
   - `requirements.txt`
   - `.streamlit/config.toml`
   - `vehicles_us.csv` dataset
2. Push all changes to GitHub.
3. Connect your GitHub repository to **Render.com** and deploy.

## Streamlit Configuration Example
In the `.streamlit/config.toml` file, add:
```
[server]
headless = true
port = 10000

[browser]
serverAddress = "0.0.0.0"
serverPort = 10000
```

## About the Project
This project was created by Mikhail Savluchinskii as a learning exercise to build a complete interactive dashboard and deploy it using Streamlit and Render.
