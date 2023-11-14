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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset():

    window.after_cancel(timer)
    canvas.itemconfig(text_timer, text="00:00")
    heading_label.config(text="Timer")
    check_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_time)
        heading_label.config(text="Long Break!", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_time)
        heading_label.config(text="Short Break!", fg=PINK)
    else:
        count_down(work_time)
        heading_label.config(text="Work!", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0 {count_sec}"
    if count_sec == 0:
        count_sec = "00"

    canvas.itemconfig(text_timer, text=f"{count_min} : {count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
            check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro App")
window.minsize(width=500, height=500)
window.config(padx=50, pady=50, bg=YELLOW)



canvas = Canvas(width=230, height=300, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(115, 150, image=tomato)
text_timer = canvas.create_text(115, 200, text="00:00", fill="white", font=("FONT_NAME", 35, "bold"))
canvas.grid(column=2, row=2)



heading_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=("FONT_NAME", 35, "bold"))
heading_label.grid(column=2, row=0)

check_label = Label(text="", fg=GREEN)
check_label.grid(column=2, row=4)

start_btn = Button(width=10, text="start", command=start_timer)
start_btn.grid(column=1, row=3)

reset_btn = Button(width=10, text="reset", command=reset)
reset_btn.grid(column=3, row=3)



window.mainloop()
