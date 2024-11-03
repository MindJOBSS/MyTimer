from tkinter import *
from math import floor

# Constants for colors and font style
PURPLE = "MediumPurple1"
GOLD = "DarkGoldenrod1"
BLUE = "aquamarine2"
FONT = ("Courier", 24, "bold")

# Variable to keep track of the timer loop for canceling if needed
timer_loop = None

# Timer start logic
def start_timer():
    # Gets the time in minutes from the entry, converts it to seconds
    count = int(entry.get()) * 60
    # Starts countdown
    count_down(count)
    # Clears entry box after starting timer
    entry.delete(0, END)

# Countdown function with recursive calls for each second
def count_down(count):
    global timer_loop
    # Calculates minutes and seconds from total count in seconds
    count_min = floor(count / 60)
    count_sec = floor(count % 60)

    # Ensures seconds display with two digits, e.g., "05"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    # Ensures minutes display as "00" if count is zero
    if count_min == 0:
        count_min = "00"
    # Updates the timer text on the canvas with formatted time
    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")

    # Continues countdown if time remains, else displays check mark
    if count > 0:
        timer_loop = window.after(1000, count_down, count - 1)
    else:
        check_label.config(text="✓")

# Reset timer logic
def reset_timer():
    global timer_loop
    # Cancels the active timer loop if running
    window.after_cancel(timer_loop)
    # Restores placeholder text in entry box
    entry.insert(END, "Enter Mins")
    # Resets the timer display to "00:00"
    canvas.itemconfig(timer, text="00:00")
    # Clears the check mark
    check_label.config(text="")
    # Clears the entry box
    entry.delete(0, END)

# UI Setup
window = Tk()
window.title("StopWatch")
# Configures background color and padding for the main window
window.config(bg=PURPLE, padx=50, pady=50)

# Canvas setup for the stopwatch background image
canvas = Canvas(width=300, height=300, bg=PURPLE, highlightthickness=0)
watch_image = PhotoImage(file="./stopwatch.png")  # Image for the timer
canvas.create_image(150, 150, image=watch_image)
canvas.grid(column=1, row=1)
# Timer text in the center of the canvas
timer = canvas.create_text(150, 150, text="00:00", font=FONT, fill=GOLD)

# Check mark label, appears after countdown ends
check_label = Label(text="", font=FONT, fg=BLUE, bg=PURPLE)
check_label.grid(column=1, row=3)

# Start button with start_timer function attached
start_button = Button(text="START", bg=PURPLE, fg=BLUE, font=FONT, command=start_timer)
start_button.grid(column=0, row=2)

# Reset button with reset_timer function attached
reset_button = Button(text="RESET", bg=PURPLE, fg=BLUE, font=FONT, command=reset_timer)
reset_button.grid(column=2, row=2)

# Timer label at the top of the UI
StopWatch_label = Label(text="Timer", fg=BLUE, bg=PURPLE, font=FONT)
StopWatch_label.grid(column=1, row=0)

# Entry box for user to input time in minutes
entry = Entry(width=10)
entry.insert(END, "Enter Mins")  # Placeholder text in entry box
entry.grid(column=1, row=2)

# Runs the Tkinter event loop
window.mainloop()
