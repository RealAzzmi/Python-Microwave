import tkinter as tk
import control

class Display:
    def __init__(self, window, width, x_pos, y_pos, font):
        self.display = tk.Entry(
            window,
            width=width,
            justify="center",  # To center the text
            font=font
            )
        self.display.configure(state="readonly")
        self.display.place(x=x_pos, y=y_pos)

class ResponseDisplay:
    def __init__(self, window, width, x_pos, y_pos, font, fg):
        self.response_display = tk.Entry(
        window,
        width=width,
        font=font,
        justify="center",
        fg=fg
        )
        self.response_display.configure(state="readonly")
        self.response_display.place(x=x_pos, y=y_pos)

class DigitButton:
    def __init__(self, window, text, x_pos, y_pos, width=2, height=1):
        self.text = text
        self.button = tk.Button(
        window,
        text=text,
        width=width,
        height=height,
        bg="black",
        fg="white",
        command=self.on_click,
        font="Helvetica 15",
        bd=0,
        highlightthickness=0
        )

        self.button.place(x=x_pos, y=y_pos)
    def on_click(self):
        control.last_clicked = int(self.text)
        control.execute()

class BooleanButton:
    def __init__(self, window, text, x_pos, y_pos,width=2, height=1):
        self.text = text
        self.button = tk.Button(
        window,
        text=text,
        width=width,
        height=height,
        command=self.on_click,
        font="Helvetica 10",
        bg="#000000",
        fg="white",
        bd=0,
        highlightthickness=0
        )
        self.button.place(x=x_pos, y=y_pos)
    
    def on_click(self):
        control.last_clicked = self.text
        control.execute()
