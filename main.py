import tkinter as tk
import control
import widget

# The window
window = tk.Tk()

# The two frames: Left (Food) and Right (Control)
food_frame = tk.Frame(window, bg="white", width=1000, height=900)
control_frame = tk.Frame(window, bg="#000000", width=400, height=900)

food_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
control_frame.pack(fill=tk.BOTH, side=tk.RIGHT, expand=True)

control.food_frame = food_frame
control.window = window

# Two displays. One is for the input of the user and the timer.
# The other is for the response of the microwave.

display = widget.Display(window, 13, 1067, 50, "Helvetica 30")
response_display = widget.ResponseDisplay(window, 45, 1050, 120, "Helvetica 10", "#2f8234")

control.display = display.display
control.response_display = response_display.response_display

# The 10 buttons represents 0 to 9

button_1 = widget.DigitButton(window, "1", 1080, 200, display.display)
button_2 = widget.DigitButton(window, "2", 1180, 200,display.display)
button_3 = widget.DigitButton(window, "3", 1280, 200, display.display)

button_4 = widget.DigitButton(window, "4", 1080, 300, display.display)
button_5 = widget.DigitButton(window, "5", 1180, 300,display.display)
button_6 = widget.DigitButton(window, "6", 1280, 300, display.display)

button_7 = widget.DigitButton(window, "7", 1080, 400, display.display)
button_8 = widget.DigitButton(window, "8", 1180, 400,display.display)
button_9 = widget.DigitButton(window, "9", 1280, 400,display.display)

button_0 = widget.DigitButton(window, "0", 1180, 500, display.display)

# The rest of the buttons

enter_button = widget.BooleanButton(window, "Enter", 1250, 490,display.display,response_display.response_display,  width=8, height=2)
backspacke_button = widget.BooleanButton(window, "⌫", 1050, 490, display.display, response_display.response_display, width=5,height=2)

manual_button = widget.BooleanButton(window, "Manual", 1130, 615,display.display,response_display.response_display ,width=10, height=2)

automatic_button = widget.BooleanButton(window, "Automatic", 1100, 750,display.display,response_display.response_display, width=14, height=2)
meat_button = widget.BooleanButton(window, "Meat", 1070, 825,display.display,response_display.response_display,width=8, height=2)
salad_vegetables = widget.BooleanButton(window, "Vegetables", 1220, 825,display.display,response_display.response_display, width=10, height=2)

# Initial response of the microwave
control.last_clicked = "Introduction"
control.execute()

window.mainloop()
