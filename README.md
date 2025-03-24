# sd_tools_project
Sptint 6. Software Developmant Tools.
Vehicle Ads Dashboard

https://github.com/misamimisa/sd_tools_project.git
https://sd-tools-project.onrender.com

Project Overview
   This project is an interactive dashboard built with Streamlit.
   It allows users to explore used car market data, apply interactive filters, and visualize key metrics.

Features

   Data loading and preprocessing with pandas:

      Missing values for is_4wd are filled with 0 and converted to boolean.
      Missing paint_color values are filled with 'unknown'.
      Missing cylinders, model_year, and odometer are filled using the median per car type using transform().

   Interactive sidebar filters:

      Car type selection
      Price range slider

   Visualizations with Plotly:

      Histogram of car prices
      Scatter plot of odometer vs. price
      Pie chart of car type distribution

Technologies Used

   Python 3
   pandas
   streamlit
   plotly.express

Installation Instructions

   1. Clone the repository:
      git clone https://github.com/misamimisa/sd_tools_project.git
   2. Navigate to the project folder:
      cd <your-project-folder> 
   3. (Optional) Create and activate a virtual environment.
   4. Install the dependencies:
      pip install -r requirements.txt
   5. Run the Streamlit app locally:
      streamlit run app.py
   6. Open your browser and go to:
      http://localhost:10000

Deployment on Render
   
   All project files are prepared for deployment.
   The .streamlit/config.toml file is configured for port 10000.
   Deployment instructions are provided in the Render dashboard.

Author
   Created by Mikhail Savluchinskii as part of a learning project on building dashboards with Streamlit.