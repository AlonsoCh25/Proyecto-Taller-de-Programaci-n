
#Video Guide : https://www.youtube.com/watch?v=D8-snVfekto&t=201s

import tkinter as tk
import requests

HEIGHT = 600
WIDTH = 450


def test_function(entry):
    print("This is the entry", entry)

#73a7e63ab29e3af5e0cdd6c57e4014be
#api.openweathermap.org/data/2.5/forecast?q={city name},{country code}

def format_response(weather):
        name = weather ["name"]
        desc = weather["weather"][0]["description"]
        temp = weather["main"]["temp"]

        return str(name) + " | " + str(desc) + " | " + str(temp)
"""
def get_weather(city):
    weather_key = "73a7e63ab29e3af5e0cdd6c57e4014be"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params ={"APPID": weather_key, "q": city, "units": "imperial"}
    response = requests.get(url, params=params)
    weather = response.json()

    label["text"] = format_response(weather)
"""
def name(name):
        print("x")

root = tk.Tk()

root.title("Space Invaders")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file="space_invaders_background.gif")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg="blue", bd=5)
frame.place(relx=0.5, rely=0.7,relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

#Set name button
button = tk.Button(frame, text="Set Name", font=40)
button.place(relx=0.7, relheight=1, relwidth=0.30)

#Level 1 button
button = tk.Button(text="Level 1", font=25)
button.place(relx = 0.1, rely=0.9, relheight=0.05, relwidth= 0.25)

#Level 2 button
button = tk.Button(text="Level 2", font=25)
button.place(relx = 0.4, rely=0.9, relheight=0.05, relwidth= 0.25)

#Level 3 button
button = tk.Button(text="Level 3", font=25)
button.place(relx = 0.7, rely=0.9, relheight=0.05, relwidth= 0.25)

#Scores _top 5_ button
button = tk.Button(text="Top scores", font=25)
button.place(relx = 0.02, rely=0.02, relheight=0.05, relwidth= 0.25)

#lower_frame = tk.Frame(root, bg="#42bff4", bd=10)
#lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.3, anchor ="n")

#label = tk.Label(lower_frame)
#label.place(relwidth=1, relheight=1)

root.mainloop()
