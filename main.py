from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- #
def timer_reset():
    global rep
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    my_label.config(text="Timer")
    check_label.config(text="")
    rep=0




# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_mech():
    global rep
    rep+=1
    work_sec=WORK_MIN*60
    short_sec=SHORT_BREAK_MIN*60
    long_sec=LONG_BREAK_MIN*60
    if rep%8==0:
        my_label.config(text="Break",fg= RED)
        count_down(long_sec)
        check_label.config(text=check_label["text"]+"✔")

    elif rep%2==0:
        my_label.config(text="Break", fg=PINK)
        count_down(short_sec)
        check_label.config(text=check_label["text"] + "✔")
    else:
        my_label.config(text="Work", fg=GREEN)
        count_down(work_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):  #we cant use while loop and time.sleep(1) because because it will keep on repeating itself and we will not be able to call the main loop.
    global timer
    min=count//60
    sec=count%60
    if count>=0:
        if sec<10 :
            sec=f"0{sec}"
        if min<10:
            min=f"0{min}"
        timer = window.after(1000,count_down,count-1)
        canvas.itemconfig(timer_text,text=f"{min}:{sec}")
    else:
        timer_mech()

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro")
window.config(padx=50,pady=50, bg=YELLOW)

canvas=Canvas(width=220,height=224,bg=YELLOW, highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(110,112,image=tomato_img)
timer_text = canvas.create_text(110,130,text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1, row=1)

my_label=Label(text="Timer", font=(FONT_NAME,50,"bold"), fg=GREEN, bg=YELLOW)
my_label.grid(column=1, row=0)


start_b=Button(text="Start", highlightthickness=0, command=timer_mech)
start_b.grid(column=0,row=2)

reset_b=Button(text="Reset", highlightthickness=0, command=timer_reset)
reset_b.grid(column=2, row=2)

check_label=Label(text="", font=(FONT_NAME,20,"bold"),fg=GREEN, bg=YELLOW)
check_label.grid(column=1,row=3)



window.mainloop()