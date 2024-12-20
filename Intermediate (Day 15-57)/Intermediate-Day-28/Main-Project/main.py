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
LONG_BREAK_MIN = 15
reps = 0
work_session = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global work_session
    reps = 0
    work_session = 0
    window.after_cancel(timer)
    check_label.config(text="", fg=GREEN)
    timer_label.config(text="TIMER", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global work_session
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 8 == 0:
        work_session += 1
        count_down(long_break_sec)
        timer_label.config(text="BREAK", fg=RED)
    elif reps % 2 != 0:
        count_down(work_sec)
        timer_label.config(text="WORK", fg=GREEN)
    elif reps % 2 == 0:
        work_session += 1
        count_down(short_break_sec)
        timer_label.config(text="BREAK", fg = PINK)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_label.config(text="✔" * work_session, fg=GREEN)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

timer_label = Label(window, text="TIMER", font=(FONT_NAME, 30, 'bold'), fg = GREEN, bg = YELLOW)
timer_label.grid(column=1, row=0)

tomato_img = PhotoImage(file = "tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text = "START", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text = "RESET", command = reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(font=(FONT_NAME, 30, 'bold'), fg = GREEN, bg = YELLOW)
check_label.grid(column=1, row=3)

window.mainloop()