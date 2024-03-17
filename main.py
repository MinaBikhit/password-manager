from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0                            # reps variable to store the current rep number
timer = None                        # timer variable to be used with the window.after and window.after_cancel methods
timer_running = False               # timer running variable to determine if the timer is running
LOGO = b'iVBORw0KGgoAAAANSUhEUgAAAMgAAADfCAYAAACzi5y9AAAEvmlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4KPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iWE1QIENvcmUgNS41LjAiPgogPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgeG1sbnM6ZXhpZj0iaHR0cDovL25zLmFkb2JlLmNvbS9leGlmLzEuMC8iCiAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyIKICAgIHhtbG5zOnBob3Rvc2hvcD0iaHR0cDovL25zLmFkb2JlLmNvbS9waG90b3Nob3AvMS4wLyIKICAgIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIKICAgIHhtbG5zOnhtcE1NPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvbW0vIgogICAgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIKICAgZXhpZjpQaXhlbFhEaW1lbnNpb249IjIwMCIKICAgZXhpZjpQaXhlbFlEaW1lbnNpb249IjIyMyIKICAgZXhpZjpDb2xvclNwYWNlPSIxIgogICB0aWZmOkltYWdlV2lkdGg9IjIwMCIKICAgdGlmZjpJbWFnZUxlbmd0aD0iMjIzIgogICB0aWZmOlJlc29sdXRpb25Vbml0PSIyIgogICB0aWZmOlhSZXNvbHV0aW9uPSI5Ni4wIgogICB0aWZmOllSZXNvbHV0aW9uPSI5Ni4wIgogICBwaG90b3Nob3A6Q29sb3JNb2RlPSIzIgogICBwaG90b3Nob3A6SUNDUHJvZmlsZT0ic1JHQiBJRUM2MTk2Ni0yLjEiCiAgIHhtcDpNb2RpZnlEYXRlPSIyMDIw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'
# LOGO variable contains the binary data of the logo image
# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    """function to stop the timer and reset the reps and Labels to default value"""
    global timer_running
    global reps
    reps = 0                                        # resetting the number of reps
    timer_running = False                           # setting timer running variable to False
    window.after_cancel(timer)                      # canceling the current timer
    check_marks.config(text="")                     # removing the current check marks
    label.config(text="Pomodoro")                   # resetting the original title
    canvas.itemconfig(timer_text, text="00:00")     # resetting the counter




# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """function that starts the timer"""
    global reps
    global timer_running
    if not timer_running:                    # condition to avoid triggering the timer while it is already running
        timer_running = True                 # setting the timer running variable to True
        reps += 1                            # increasing the number of reps
        work_secs = WORK_MIN * 60                   # changing work time from minutes to secs
        long_break_secs = LONG_BREAK_MIN * 60       # changing long break time from minutes to secs
        short_break_secs = SHORT_BREAK_MIN * 60     # changing short break time from minutes to secs

        if reps % 8 == 0:                           # triggering a long break after multiples of 8 reps pass
            label.config(text= "Break", fg=RED)
            count_down(long_break_secs)
        elif reps % 2 == 0:                         # triggering a short break every 2 reps until 8 then a long break is triggered
            label.config(text="Break", fg=PINK)
            count_down(short_break_secs)
        else:                                       # triggering work time
            label.config(text="Work", fg=GREEN)
            count_down(work_secs)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    """function that counts down and updates the timer on screen"""
    global reps
    global timer
    count_min = math.floor(count / 60)        # using the floor method from math module we can get the remaining number of minutes after the division
    count_sec = round(count % 60)             # using mod to determine the number of secs remaining in the fractured minute
    if count_sec < 10:
        count_sec = f"0{count_sec}"           # using dynamic typing to correct the values under 10 to show in 00 format
    if count_min < 10:
        count_min = f"0{count_min}"           # using dynamic typing to correct the values under 10 to show in 00 format



    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")      # displaying the new value for min and secs
    if count > 0:
        timer = window.after(1000, count_down, count - 1)     # recalling the counter if timer remaining > 0
    else:
        start_timer()               # calling the start timer when the timer is done to start the following phase
        marks = ""                  # variable to hold the check marks for displaying
        work_sessions = math.floor(reps/2)      # getting the number of completed sessions
        for _ in range (work_sessions):         # generating a ✓ for every completed session
            marks += "✓"
            check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()                                   # creating a window object from the TK class
window.title("Pomodoro")                        # choosing the window title
window.config(padx=100, pady=50, bg=YELLOW)     # adding padding and choosing background colour for the window


# Creating a canvas for the image
canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)         # creating a canvas for the image and setting dimension and colors
tomato = PhotoImage(data=LOGO)                              # setting the desired image through LOGO variable
canvas.create_image(102, 112, image=tomato)           # loading the image into the canvas
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")) # over laying the timer text
canvas.grid(row=1, column=1)            # choosing alignment in the grid

# Creating a label
label = Label(text="Pomodoro", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50), width= 8)  # creating a Label and choosing text, foreground color, background color and font
label.grid(row=0, column=1)   # choosing alignment in the grid


# Creating a start button
start_button = Button(text="Start", command=start_timer)   # creating a start button and assigning it to start_timer function
start_button.grid(row=2, column=0)       # choosing alignment in the grid

# Creating a reset button
start_button = Button(text="Reset", command=reset_timer)   # creating a reset button and assigning it to reset_timer function

start_button.grid(row=2, column=2)      # choosing alignment in the grid

# creating a tick
check_marks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))   # creating a label for the session completion check marks
check_marks.grid(row=3, column=1)        # choosing alignment in the grid


window.mainloop()                      # main loop to keep the window from closing
