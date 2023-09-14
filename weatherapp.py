import tkinter as tk
from tkinter import font
import requests
from PIL import ImageTk as itk

HEIGHT = 500
WIDTH = 600

def test_function(entry):
    print("This is the entry:", entry)

#aeafdac344956ace31c5beae8cde7312
#https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature(in Degree Celsius): %s' % (name,desc,temp)
    except:
        final_str = 'There was an error retrieving that information'

    return final_str


def get_weather(city):
    weather_key = 'aeafdac344956ace31c5beae8cde7312'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID':weather_key, 'q':city, 'units':'metric'}
    response = requests.get(url,params=params)
    weather=response.json()

    label['text'] = format_response(weather)


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = itk.PhotoImage(file="istockphoto-863513024-2048x2048.jpg")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#4FAAF6', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Comic Sans MS', 12))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=('Comic Sans MS', 12), command=lambda: get_weather(entry.get()))  #lambda func is used so that it can redefined everytime we use it
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#4FAAF6', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Comic Sans MS', 12), anchor='nw',justify='left',bd=4)
label.place(relwidth=1, relheight=1)

root.mainloop()