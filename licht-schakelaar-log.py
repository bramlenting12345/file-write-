import tkinter as tk

scherm = tk.Tk()
log_status = open('actions.log' , 'a')

x = ["uit"]

def knop_switch():
    if x[0]== "uit":
        x[0] = "aan"
        log_status.write(x[0])
        log_status.write('\n')

        scherm.configure(background="yellow")
        knop.configure(text="licht is aan ")
    else: 
        x[0] = "uit"
        log_status.write(x[0])
        log_status.write('\n')

        scherm.configure(background="black")
        knop.configure(text="licht is uit")


scherm.configure(padx=100,pady=100)
knop = tk.Button(text='knop', bg="yellow", fg="black",command=knop_switch,height=1,width=15)
knop.pack()
titel = tk.Label(text="gemaakt door Bram",bg="purple",fg="orange",height=1,width=20)
titel.pack(side="top")


scherm.mainloop()
