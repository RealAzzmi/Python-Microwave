import tkinter as tk
import time

food_frame = None
window = None
display = None
response_display = None

last_clicked = None
last_2_clicked = None
temperature = 0
duration = 0
weight = 0

def rgb_to_hex(r,g,b):
    return f"#{r:02x}{g:02x}{b:02x}"

def print_response(display_input, message):
    display_input.configure(state="normal")
    display_input.delete(0, tk.END)
    display_input.insert(0, message)
    display_input.configure(state="readonly")

def digits_pressed(digit):
    try:
        new_number = int(display.get()) * 10 + digit
    except:
        new_number = digit
    print_response(display, new_number)
def run(duration_inp):
    global duration, temperature, weight, last_clicked, last_2_clicked

    tmp = 255
    decrement_value = max(int(255 / duration_inp), 1)
    counter = duration_inp 
    while counter > 0:
        print_response(display, time.strftime("%H:%M:%S", time.gmtime(counter)))
        food_frame.configure(bg=rgb_to_hex(255, int(tmp*0.7), tmp))
        food_frame.update()
        display.update()
        time.sleep(1)
        counter -= 1
        tmp -= decrement_value
        tmp = max(0, tmp)
    print_response(display, "00:00:00")
    print_response(response_display, "Finished!")

    last_clicked = None
    last_2_clicked = None
    temperature = 0
    duration = 0
    weight = 0

def execute():
    global last_2_clicked, temperature, duration

    if isinstance(last_clicked, int):
        digits_pressed(last_clicked)
    elif last_clicked == "⌫":
        print_response(display, display.get()[:-1])
    elif last_clicked == "Introduction":
        print_response(response_display, "Manual or Automatic (Defrost/Cook/Reheat)?")
    elif last_clicked == "Manual":
        last_2_clicked = "Manual"
        print_response(response_display, "Enter the temperature in °C!")
    elif last_clicked == "Defrost\nMeat":
        last_2_clicked = "Defrost\nMeat"
        print_response(response_display, "Enter the mass in pounds (lb)!")
    elif last_clicked == "Defrost\nVegetables":
        last_2_clicked = "Defrost\nVegetables"
        print_response(response_display, "Enter the mass in ounces (℥)!")
    elif last_clicked == "Cook":
        duration = 20 * 60 # 20 minutes
        print_response(response_display, f"Default Temperature = 100 °C  -  Duration = {duration} s")
        run(duration)
    elif last_clicked == "Reheat":
        duration = 3 * 60 # 3 minutes
        print_response(response_display, f"Default Temperature = 80 °C  -  Duration = {duration} s")
        run(duration)
    elif last_clicked == "Enter":
        if last_2_clicked == "Manual":
            if temperature == 0:
                temperature = int(display.get())
                print_response(display, "")
                print_response(response_display, "Enter the duration in seconds!")
            else:
                duration = int(display.get())
                print_response(response_display, f"Temperature = {temperature} °C  -  Duration = {duration} s")
                run(duration)
        elif last_2_clicked == "Defrost\nMeat":
            weight = int(display.get())
            duration = 9 * weight * 60
            print_response(response_display, f"Default Temperature = 60 °C  -  Duration = {duration} s")
            run(duration)
        elif last_2_clicked == "Defrost\nVegetables":
            weight = int(display.get())
            duration = weight * 60
            print_response(response_display, f"Default Temperature = 60 °C  -  Duration = {duration} s")
            run(duration)


            
