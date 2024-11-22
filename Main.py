import requests
import streamlit as st

# Prepare API key and API url
api_key = "ZFKgoV36lGH79JlZvdu3exISofzon8Iipu2vJcq7"
url = ("https://api.nasa.gov/planetary/apod?"\
       "api_key=ZFKgoV36lGH79JlZvdu3exISofzon8Iipu2vJcq7")

# Get the request data
request = requests.get(url)
# Set a request data as a dictionary
data = request.json()

# Extract the image title, url and explanation
title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

# Download the image
image_filepath = "img.jpg"
response = requests.get(image_url)
with open(image_filepath, "wb") as file:
       file.write(response.content)


