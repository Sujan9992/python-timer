from math import floor
from tkinter import Button, Canvas, PhotoImage, Scale, Tk

time: int = 0
timer: str | None = None
FONT = "Consolas"

win: Tk = Tk()
win.title("Timer")
win.config(padx=50, pady=25, bg="white")


def scale_used(value):
    global time
    time = int(value)


scale = Scale(from_=1, to=60, command=scale_used)
scale.config(orient="horizontal", bg="white", border=0)
scale.grid(column=1, row=0)


def start_counter():
    counter(time * 60)


def reset_counter():
    win.after_cancel(timer)
    canvas.itemconfig(canvas_text, text="00:00")


def counter(count):
    min = floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(canvas_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = win.after(1000, counter, count - 1)


canvas = Canvas(width=100, height=183, bg="white", highlightthickness=0)
img = PhotoImage(file="Timer/hourglass.png")
canvas.create_image(50, 93, image=img)
canvas_text = canvas.create_text(
    50, 93, text="00:00", fill="black", font=(FONT, 20, "bold")
)
canvas.grid(column=1, row=1, padx=20, pady=20)

start_btn = Button(text="Start", bg="white", command=start_counter)
start_btn.grid(column=0, row=1)

reset_btn = Button(text="Reset", bg="white", command=reset_counter)
reset_btn.grid(column=3, row=1)

win.mainloop()
