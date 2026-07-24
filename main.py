# -*- coding: utf-8 -*-

from Tkinter import *
import time

# -------------------------
# Variables
# -------------------------
running = False
start_time = 0
elapsed_time = 0

# -------------------------
# Update Timer
# -------------------------
def update():
    global elapsed_time

    if running:
        elapsed_time = time.time() - start_time

        hours = int(elapsed_time / 3600)
        minutes = int((elapsed_time % 3600) / 60)
        seconds = int(elapsed_time % 60)
        milliseconds = int((elapsed_time * 100) % 100)

        timer.config(
            text="%02d:%02d:%02d.%02d"
            % (hours, minutes, seconds, milliseconds)
        )

        root.after(10, update)


# -------------------------
# Start Stopwatch
# -------------------------
def start():
    global running, start_time

    if not running:
        running = True
        start_time = time.time() - elapsed_time
        status.config(text="Status : Running", fg="green")
        update()


# -------------------------
# Stop Stopwatch
# -------------------------
def stop():
    global running

    running = False
    status.config(text="Status : Stopped", fg="red")


# -------------------------
# Reset Stopwatch
# -------------------------
def reset():
    global running, elapsed_time

    running = False
    elapsed_time = 0

    timer.config(text="00:00:00.00")
    status.config(text="Status : Reset", fg="orange")


# -------------------------
# Main Window
# -------------------------
root = Tk()

root.title("Professional Stopwatch")
root.geometry("500x320")
root.resizable(False, False)
root.configure(bg="#1E1E1E")

# -------------------------
# Heading
# -------------------------
heading = Label(
    root,
    text="PROFESSIONAL STOPWATCH",
    font=("Arial", 20, "bold"),
    bg="#1E1E1E",
    fg="cyan"
)

heading.pack(pady=20)

# -------------------------
# Timer Display
# -------------------------
timer = Label(
    root,
    text="00:00:00.00",
    font=("Courier New", 30, "bold"),
    bg="#1E1E1E",
    fg="white"
)

timer.pack(pady=20)

# -------------------------
# Buttons
# -------------------------
frame = Frame(root, bg="#1E1E1E")
frame.pack()

start_btn = Button(
    frame,
    text="Start",
    width=10,
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    command=start
)

start_btn.grid(row=0, column=0, padx=10)

stop_btn = Button(
    frame,
    text="Stop",
    width=10,
    font=("Arial", 12, "bold"),
    bg="red",
    fg="white",
    command=stop
)

stop_btn.grid(row=0, column=1, padx=10)

reset_btn = Button(
    frame,
    text="Reset",
    width=10,
    font=("Arial", 12, "bold"),
    bg="orange",
    fg="white",
    command=reset
)

reset_btn.grid(row=0, column=2, padx=10)

# -------------------------
# Status Label
# -------------------------
status = Label(
    root,
    text="Status : Ready",
    font=("Arial", 12, "bold"),
    bg="#1E1E1E",
    fg="white"
)

status.pack(pady=30)

# -------------------------
# Footer
# -------------------------
footer = Label(
    root,
    text="Developed by Aprupinath Singh",
    font=("Arial", 9),
    bg="#1E1E1E",
    fg="gray"
)

footer.pack(side=BOTTOM, pady=10)

# -------------------------
# Run
# -------------------------
root.mainloop()