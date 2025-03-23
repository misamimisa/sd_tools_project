# sd_tools_project
Sptint 6. Software Developmant Tools.
Vehicle Ads Dashboard

Project Description:

This project is an interactive data visualization dashboard built with Streamlit, using a dataset of vehicle advertisements from the US market. The app allows users to explore car listings and analyze vehicle attributes through interactive charts and graphs.

Key Features:

Interactive histograms showing the distribution of car prices, model years, and mileage.

Scatter plots to visualize relationships between vehicle price, year, and odometer readings.

A dynamic pie chart displaying the share of vehicle types.

Filtering options using checkboxes to include or exclude outliers or specific car types.

Dropdown menus and widgets for flexible and user-friendly data exploration.

Technologies & Libraries Used:

    Python 3.11

    Pandas

    Streamlit

    Plotly Express

    Seaborn (used for experimentation in Jupyter)

    ipywidgets (used for notebook exploration)

Project Structure

├── app.py
├── vehicles_us.csv
├── requirements.txt
└── README.md

How to Run This Project Locally

Clone the repository:

git clone <https://github.com/misamimisa/sd_tools_project.git>
cd <your_project_folder>

Create and activate a virtual environment:

    python -m venv my_env
    my_env\Scripts\activate (on Windows)
    source my_env/bin/activate (on macOS/Linux)

Install the required libraries:

    pip install -r requirements.txt

Run the Streamlit app:

    streamlit run app.py

Data Source:

The dataset used in this project is vehicles_us.csv, containing information about car ads, including price, year, condition, odometer, and other attributes.

Author:

Created by Mikhail Savluchinskii as part of a TripleTen project.