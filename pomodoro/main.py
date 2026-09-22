import math
from  tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer = NONE
# ---------------------------- TIMER RESET ------------------------------- # 
def new():
    window.after_cancel (timer)
    canvas.itemconfig(canvas_text, text="00:00")
    label.config(text="Timer", fg=PINK)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_time ():
    global reps
    reps+=1
    if reps % 8 == 0:
        count_down(20 * 60)
        label.config(text="Long_break", fg=RED)

    elif reps % 2 == 0 :
        count_down(5 * 60)
        label.config(text="Short_rest", fg=PINK)
    else:
        count_down(25*60)
        label.config(text="Work",fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    if count>=0:
         global timer
         timer=window.after(1000,count_down,count-1)
         minutes=math.floor(count/60)
         if minutes<10:
             minutes=f"0{minutes}"
         seconds=count%60
         if seconds<10:
             seconds=f"0{seconds}"

         canvas.itemconfig(canvas_text,text=f"{minutes}:{seconds}")
    else:
        start_time()
# ---------------------------- UI SETUP ------------------------------- #
#window
window=Tk()
window.title(string="Pomodoro")
window.config(bg=YELLOW)
#label
label=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,30,"normal"))
label.grid(row=0,column=1)
#canvas
canvas=Canvas(width=200,height=223,bg=YELLOW,highlightthickness=0)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(100,110,image=tomato)
canvas_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

#start_button
start_button=Button(text="start",command=start_time)
start_button.grid(row=2,column=0)
#restart_button
restart_button=Button(text="restart",command=new)
restart_button.grid(row=2,column=2)
#mark
mark=Label(bg=YELLOW)
mark.grid(row=2,column=1)
window.mainloop()