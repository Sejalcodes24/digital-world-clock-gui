import tkinter as tk
window = tk.Tk()
window.title("Digital clock")
window.geometry("700x400")
window.configure(bg = "#497182")

import pytz
from datetime import datetime
from tkinter import PhotoImage


frame = tk.Frame(window , bg = "#497182")
frame.pack(side = "left", expand = True , fill = "both")

label4 = tk.Label(frame, text = "India Time" , font = ("Helvetica" , 45 , "bold") , fg = "black")
label4.pack(pady = 20)

label = tk.Label(frame, text = "" , font = ("Helvetica" , 38 , "bold"), fg = "black")
label.pack(pady = 25) 

selected_option = tk.StringVar()
selected_option.set(0)

time_format = tk.Radiobutton(window, text = " 12 Hour clock " , variable = selected_option , value = "12-hour",font = ("Helvetica" , 18 , "bold") , fg = "black" )
time_format.pack(pady = 20)
time_format2 = tk.Radiobutton(window, text = " 24 Hour clock " , variable = selected_option , value = "24-hour",font = ("Helvetica" , 18 , "bold") , fg = "black" )
time_format2.pack(pady = 20)

def update_time():
    india_time = datetime.now(pytz.timezone("Asia/Kolkata"))
    if selected_option.get() == "12-hour":
        formatted_time = india_time.strftime("%I:%M:%S %p")
    else:
        formatted_time = india_time.strftime("%H:%M:%S")
    label.config(text = formatted_time )

    window.after(1000, update_time)

update_time()

image = PhotoImage(file = "india.png")
label5 = tk.Label(frame, image = image )
label5.pack(pady = 10)


frame2 = tk.Frame(window ,bg = "#497182")
frame2.pack(side = "right", expand = True , fill = "both")

flag_label = tk.Label(frame2 , image = image  )
flag_label.pack(pady = 10)

label3 = tk.Label(frame2 , text = "Selected Country Time" , font = ("Helvetica" , 40 , "bold") , fg = "black")
label3.pack(pady = 10)

label2 = tk.Label(frame2, text = "" , font = ("Helvetica" ,40 , "bold"), fg = "black")
label2.pack(pady = 10)

options = ["Oman" , "USA", "Japan"]
variable = tk.StringVar()
variable.set("Oman")

Option_menu = tk.OptionMenu(frame2 , variable , *options )
Option_menu.config(font = ("Helvetica" , 20 , "bold"), fg = "black") 
Option_menu.pack(pady = 10)



def update_time2():
    country = variable.get()
    zones = {
        "Oman" : "Asia/Muscat",
        "USA"  :  "America/New_York",
        "Japan" : "Asia/Tokyo"
    }
    
    selected_zone = zones[country]
    current_time = datetime.now(pytz.timezone(selected_zone))
    if selected_option.get() == "12-hour":
        formatted_time = current_time.strftime("%I:%M:%S %p")
    else:
        formatted_time = current_time.strftime( "%H:%M:%S")
    label2.config(text = formatted_time )
    
    
    flag = variable.get().lower()  # to make usa and USA both work
    image = PhotoImage(file = f"{flag}.png")
    flag_label.config(image = image )
    flag_label.image = image

    window.after(1000, update_time2)



update_time2()

window.mainloop()



