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
def run(duration):
    tmp = 255
    decrement_value = max(int(255 / duration), 1)
    counter = duration 
    while counter > 0:
        print_response(display, str(counter))
        food_frame.configure(bg=rgb_to_hex(255, int(tmp*0.7), tmp))
        food_frame.update()
        display.update()
        time.sleep(1)
        counter -= 1
        tmp -= decrement_value
        tmp = max(0, tmp)
    print_response(display, "0")
    print_response(response_display, "Finished!")

def execute():
    global last_2_clicked, temperature, duration

    if isinstance(last_clicked, int):
        digits_pressed(last_clicked)
    elif last_clicked == "⌫":
        print_response(display, display.get()[:-1])
    elif last_clicked == "Introduction":
        print_response(response_display, "Manual or Automatic?")
    elif last_clicked == "Manual":
        last_2_clicked = "Manual"
        print_response(response_display, "Enter the temperature in °C!")
    elif last_clicked == "Enter":
        if last_2_clicked == "Manual":
            if temperature == 0:
                temperature = int(display.get())
                print_response(response_display, "Enter the duration in seconds!")
            else:
                duration = int(display.get())
                print_response(response_display, f"Temperature = {temperature} °C  -  Duration = {duration} s")
                run(duration)
