import streamlit as st
import plotly.express as px
from Backend import get_data

# Add title, text input, slider, selectbox, and subheader
st.title("Weather Forecast For the next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forcasted days")
option = st.selectbox("Select data to view",("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}.")

# If place se pone para que no aparezca un error cuando quede vacío el textbox
if place:
    # Get the temperature/sky data
    try:
        data = get_data(place, days)

        filtered_data = get_data(place, days)

        if option == "Temperature":
            # Create a temperature plot
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y":"temperatures (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear":"Images/clear.png", "Clouds":"images/cloud.png", "Rain":"images/rain.png",
                      "Snow":"images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)
    except KeyError:
        st.write("That place doesn't exist")
