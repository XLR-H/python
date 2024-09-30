from tkinter import *


def submit():
    print('the temperature is: '+ str(scale.get())+' degrees')


window = Tk()

scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              font=('comic sans ms',20),
              tickinterval=10,
              resolution=5, #increment slider
              troughcolor='#6ef'
              )
scale.pack()

button = Button(window, text='submit',command=submit)
button.pack()

window.mainloop()