# ----- Imports ----- 
from tkinter import *
import tkinter as tk
import requests

# ----- Global Variables -----
height = 500
width = 600
background_color = "#80C1FF"

# Get Your API Key From openweatherapp.org
# api.openweathermap.org/data/2.5/weather?q = {city name}, {country code}

# ----- Functions -----
def format_response(weather):
	"""Formats The HTTP Response To A String"""
	try:
		name = weather['name']
		desc = str(weather['weather'][0]['description']).capitalize()
		temp = weather['main']['temp']

		final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (name, desc, temp)
	except:
		final_str = 'There Was A Problem\nRetrieving That Information'
		
	return final_str

def get_weather(city):
	"""Gets The Weather From The Input"""
	weather_key = 'api_key'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
	response = requests.get(url, params = params)
	weather = response.json()

	label1['text'] = format_response(weather)

# ----- Main Code -----

# Initializing The Main Tkinter Window
root = tk.Tk()
root.title("Weather App")
root.geometry(f"{width}x{height}")

# Initializing And Setting The Images
logo_image = tk.PhotoImage(file = "Logo.png")
background_image = tk.PhotoImage(file = 'Background.png')
root.iconphoto(False, logo_image)
root.iconbitmap("Icon.ico")
background_label = tk.Label(root, image = background_image)
background_label.place(relwidth = 1, relheight = 1)

# Creating The Main Window
frame1 = tk.Frame(root, bg = background_color, bd = 5, relief = RIDGE)
frame1.place(relx = 0.5, rely = 0.1, relwidth = 0.75, relheight = 0.1, anchor = 'n')

entry1 = tk.Entry(frame1, font = ("Times New Roman", 20), relief = RIDGE)
entry1.place(relx = 0.02, rely = 0.1, relwidth = 0.6, relheight = 0.8)

button1 = tk.Button(frame1, text = "Get Weather", font = ("Times New Roman", 18), relief = RIDGE, command = lambda:get_weather(entry1.get()), cursor = "hand2")
button1.place(relx = 0.68, rely = 0.1, relwidth = 0.3, relheight = 0.8)

frame2 = tk.Frame(root, bg = background_color, bd = 10, relief = RIDGE)
frame2.place(relx = 0.5, rely = 0.25, relwidth = 0.75, relheight = 0.6, anchor = 'n')

label1 = tk.Label(frame2, font = ("Courier", 18), relief = RIDGE)
label1.place(relwidth = 1, relheight = 1)

# ----- Driver Code -----
if __name__ =  = "__main__":
	root.mainloop()
