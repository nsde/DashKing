import os
import tkinter
import win32api # for screen resolution 

# WINDOW
win = tkinter.Tk()
win.title("DashKing")
win.config(bg="#F87F06")
win.geometry("720x720")
win.tk.call('wm', 'iconphoto', win._w, tkinter.PhotoImage(file=os.getcwd() + '\\src\\crown.png'))

# COMMANDS
def start():
    pass

def info():
    pass

# GUI
startBtn = tkinter.Button(win, text="Start", command=start, font=("Showcard Gothic", 50), fg="white", bg="#C76502", relief="flat", activeforeground="white", activebackground="#F87F06").pack()
startBtn = tkinter.Button(win, text="Infos", command=info, font=("Showcard Gothic", 50), fg="white", bg="#C76502", relief="flat", activeforeground="white", activebackground="#F87F06").place(rely=-2, anchor="center")

win.mainloop()