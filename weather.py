from tkinter import *
import tkinter as tk
from tkinter import Message, Text
import requests

def VCR_TECHDOT():
        print("IF YOU LIKE THE CONTENT THEN LIKE THE VIDEO")
        print("IF YOU'RE NOT SUBSCRIBED MY CHANNEL THEN WHY ARE YOU WAITING FOR??\n JUST HIT THAT SUBSCRIBE BUTTON")
        print("IF YOU THINK THIS IS GOING TO BE HELPFUL TO ANYONE THEN SHARE WITH THEM.\n\n")

# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# a4aa5e3d83ffefaba8c00284de6ef7c3

def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
	except:
		final_str = 'There was a problem retrieving that information'

	return final_str

def get_weather(city):
	weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
	response = requests.get(url, params=params)
	weather = response.json()

	label['text'] = format_response(weather)

window = tk.Tk()
photo=PhotoImage(file="vcr_techdot.png")
canvas = tk.Canvas(window, height=650, width=900,bg='black')
canvas.pack()

window.title("Weather Detection Project Window") 
window.configure(bg ="black") 
window.grid_rowconfigure(1, weight = 1) 
window.grid_columnconfigure(1, weight = 1)

message= tk.Label(window,text='Weather-Detection\n(Using Python)',bg='black',fg ="red",
                  width=20, height=2,font = ('Arial', 30, ' bold '))
message.place(relx=0.5, rely=0, relwidth=0.85, relheight=0.2, anchor='n')

frame = tk.Frame(window, bg='red', bd=5)
frame.place(relx=0.5, rely=0.25, relwidth=0.85, relheight=0.1, anchor='n')

frame2 = tk.Frame(window, bg='yellow', bd=10)
frame2.place(relx=0.5, rely=0.85, relwidth=0.8, relheight=0.1, anchor='n')

message2 = tk.Label( frame2, text ="Created by VCR TECHDOT",
                    bg='black', fg = "yellow", font = ('arial', 20, 'bold'))        
message2.place(relx = 0.5, rely = 0,relwidth=1,relheight=1, anchor='n')

entry= tk.Entry(frame, bg ="yellow", fg ="red", font = ('Arial', 15, ' bold ')) 
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text ="Get Weather",  
command = lambda: get_weather(entry.get()), fg ="Red", bg ="black",  
activebackground = "Red",  font =('arial', 14, ' bold ')) 
button.place(relx=0.68, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(window, bg='red',bd=50)
lower_frame.place(relx=0.5, rely=0.4, relwidth=0.85, relheight=0.4, anchor='n')

label = tk.Label(lower_frame,bg='black',fg ="red", font = ('Arial', 15, ' bold '))
label.place(relwidth=1, relheight=1)

quitWindow = tk.Button(lower_frame, text ="QUIT",  
command = window.destroy, fg ="red", bg ="yellow",  
width = 5, height = 2, activebackground = "Red",  
font =('fixedsys', 15, ' bold ')) 
quitWindow.place(relx=.94, rely=1)

TECHDOT = tk.Button(window,  command = VCR_TECHDOT, bg ="blue",  
image=photo,width=60,height=70, activebackground = "Red",) 
TECHDOT.place(relx=.92, rely=.85)

window.mainloop()
