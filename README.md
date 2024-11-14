# Weather Forecast API

This is a simple weather forecasting application built using Python and Streamlit. It allows users to view temperature and sky conditions for a selected location over a specified number of days. The app uses data from the OpenWeatherMap API and visualizes the forecast using Plotly for temperature trends or displays relevant weather icons for sky conditions.
Features

    Temperature Forecast: View the temperature for a selected city over the next 1-5 days.
    Sky Condition Forecast: View sky conditions (Clear, Cloudy, Rain, Snow) over the next 1-5 days.
    Interactive Interface: Users can input the city, select the number of forecast days, and choose between temperature or sky conditions to visualize.
    Plotly Integration: Line plots are used to visualize temperature changes.
    Weather Icons: Icons are shown for different sky conditions like clear sky, cloudy, rain, and snow.

Prerequisites

Before running the application, make sure you have the following installed:

    Python 3.x
    Streamlit
    Plotly
    Requests
    OpenWeatherMap API Key (You'll need to sign up for an API key from OpenWeatherMap).

Python Libraries

You can install the necessary Python libraries using pip:

bash

pip install streamlit plotly requests

Files
1. Backend.py

This file contains the function to fetch weather data from the OpenWeatherMap API and returns a filtered set of results for a given city and number of forecast days.
Functionality:

    get_data(): Fetches weather data from OpenWeatherMap's API for the specified city and number of days. It returns a filtered forecast of either temperature or sky conditions.

2. Main.py

This file runs the Streamlit app, allowing users to interact with the application. It provides an interface for inputting the city name, selecting forecast days, and viewing either temperature trends or sky conditions.
Features:

    Input field: Allows users to input the city they want to forecast.
    Slider: Allows the user to choose how many days to forecast (1 to 5).
    Select Box: Lets the user choose between viewing Temperature or Sky conditions.
    Plotly Chart: Renders a line plot for temperature forecasts.
    Images: Displays weather icons for sky conditions like Clear, Clouds, Rain, and Snow.

Running the Application

    Clone this repository:

    bash

git clone https://github.com/your-repo/weather-forecast-app.git

Navigate to the project directory:

bash

cd weather-forecast-app

Run the Streamlit application:

bash

    streamlit run Main.py

    Open your browser and go to the URL provided by Streamlit (usually http://localhost:8501).

Example Usage

    Enter the city name (e.g., "Tokyo").
    Use the slider to select the number of forecast days (e.g., 3 days).
    Select whether you want to see the temperature plot or the sky condition icons.
    The application will fetch and display the data accordingly.

API Key

Make sure to replace the placeholder API_key in the Backend.py file with your actual OpenWeatherMap API key:

python

API_key = "your_openweathermap_api_key"
