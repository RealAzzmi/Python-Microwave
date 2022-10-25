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

# The 10 buttons represent 0 to 9

button_1 = widget.DigitButton(window, "1", 1080, 200)
button_2 = widget.DigitButton(window, "2", 1180, 200)
button_3 = widget.DigitButton(window, "3", 1280, 200)

button_4 = widget.DigitButton(window, "4", 1080, 300)
button_5 = widget.DigitButton(window, "5", 1180, 300)
button_6 = widget.DigitButton(window, "6", 1280, 300)

button_7 = widget.DigitButton(window, "7", 1080, 400)
button_8 = widget.DigitButton(window, "8", 1180, 400)
button_9 = widget.DigitButton(window, "9", 1280, 400)

button_0 = widget.DigitButton(window, "0", 1180, 500)

# The rest of the buttons

enter_button = widget.BooleanButton(window,"Enter", 1250, 490, width=8, height=2)
backspacke_button = widget.BooleanButton(window, "⌫", 1050, 490, width=5,height=2)

manual_button = widget.BooleanButton(window, "Manual", 1130, 585, width=10, height=2)

defrost_meat_button = widget.BooleanButton(window, "Defrost\nMeat", 1070, 825, width=8, height=2)
defrost_vegetables_button = widget.BooleanButton(window, "Defrost\nVegetables", 1220, 825, width=10, height=2)

reheat_button = widget.BooleanButton(window, "Reheat", 1130, 665, width=10, height=2)
cook_button = widget.BooleanButton(window, "Cook", 1130, 735, width=10, height=2)

# Initial response of the microwave
control.last_clicked = "Introduction"
control.execute()

window.mainloop()
