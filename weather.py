from tkinter import *
import requests
import tkinter as tk
from PIL import ImageTk, Image

def get_weather():
    city = city_name.get()

    #read the README file for the api key generation

    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=ed4aba0472ffc6ad7429ab08055e2bb2"+"&units=metric").json()
    print(data)
    lbl_11.config(text=data["main"]["temp"],fg="black")
    lbl_21.config(text=data["main"]["humidity"],fg="black")
    lbl_31.config(text=data["wind"]["speed"],fg="black")
    lbl_41.config(text=data["wind"]["deg"],fg="black")
    lbl_51.config(text=data["weather"][0]["description"],fg="black")

root = tk.Tk()
root.title("Weather Forecast using API")
root.geometry("600x600")

bg_image = ImageTk.PhotoImage(Image.open("weather.jpg"))

#display the background image
background_label = tk.Label(root, image=bg_image, height=600, width=600)
background_label.place(x=0, y=0)


city_name = tk.StringVar()

box = tk.Label(root, text="Enter city name or pincode:", font=("Times", 20), bg="lightblue")
box.place(x=50, y=40)

box = tk.Entry(root, textvariable=city_name, relief='solid',font=("Times", 18))
box.place(x=380, y=40, height=35, width=200)

lbl_1 = Label(root, text="Temperature:", font=("Times", 15), bg="lightblue")
lbl_1.place(x=150, y=200, height=50, width=110)
lbl_11 = Label(root, text="in celsius", font=("Times", 15), fg="grey")
lbl_11.place(x=310, y=200, height=50, width=120)

lbl_2 = Label(root, text="Humidity:", font=("Times", 15), bg="lightblue")
lbl_2.place(x=150, y=260, height=50, width=110)
lbl_21 = Label(root, text="in percent", font=("Times", 15), fg="grey")
lbl_21.place(x=310, y=260, height=50, width=120)

lbl_3= Label(root, text="Wind speed:", font=("Times", 15), bg="lightblue")
lbl_3.place(x=150, y=320, height=50, width=110)
lbl_31 = Label(root, text="in m/s", font=("Times", 15), fg="grey")
lbl_31.place(x=310, y=320, height=50, width=120)

lbl_4= Label(root, text="Wind degree:", font=("Times", 15), bg="lightblue")
lbl_4.place(x=150, y=380, height=50, width=110)
lbl_41 = Label(root, text="in degrees", font=("Times", 15), fg="grey")
lbl_41.place(x=310, y=380, height=50, width=120)


lbl_5 = Label(root, text="Description:", font=("Times", 15), bg="lightblue")
lbl_5.place(x=150, y=440, height=50, width=110)
lbl_51 = Label(root, text="climate type", font=("Times", 15), fg="grey")
lbl_51.place(x=310, y=440, height=50, width=120)

#button for getting weather data
btn = Button(root, text="Get Weather Data", command=get_weather, font=("Times", 16), bd=2, relief='solid')
btn.place(x=225, y=100, height=30, width=180)

root.mainloop()