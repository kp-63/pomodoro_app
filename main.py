from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
window_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global window_timer
    window.after_cancel(window_timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    tick.config(text="")
    global reps
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps+=1
    work_min_sec = WORK_MIN*60
    short_sec = SHORT_BREAK_MIN*60
    long_sec = LONG_BREAK_MIN*60

    if reps%8==0:
        count_down(long_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps%2==0:
        count_down(short_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_min_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min= math.floor(count/60)
    sec= count%60
    if sec<10:
        sec=f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count>0:
        global window_timer
        window_timer = window.after(1000,count_down,count-1 )
    else:
        start_timer()
        mark=""
        work_session = math.floor(reps/2)
        for i in range(work_session):
             mark+="✔"
        tick.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomorodo")
window.config(padx=100, pady=100, bg=YELLOW)

timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
timer_label.grid(column=2, row=1)


start = Button(text="Start", fg=PINK, font=(FONT_NAME, 15), command=start_timer)
start.grid(column=1, row=3)

reset = Button(text="Reset", fg=PINK, font=(FONT_NAME, 15), command=reset_timer)
reset.grid(column=3, row=3)

tick = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
tick.grid(column=2, row=4)

canvas = Canvas(width=200, height=224, bg= YELLOW, highlightthickness=0)
tomato= PhotoImage(file="tomato.png")
canvas.create_image(100, 110, image=tomato)
timer_text=canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=2, row=2)



window.mainloop()
