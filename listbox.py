from tkinter import *

def submit():
    print('you have ordered: ')
    print(listbox.get(listbox.curselection()))


window = Tk()


listbox = Listbox(window,
                  bg='#f7ffde',
                  font=('constantia',35),
                  width=12
                  )
listbox.pack()

listbox.insert(1,'burger')
listbox.insert(2,'hotdog')
listbox.insert(3,'madmeat')
listbox.insert(4,'ommelet')
listbox.insert(5,'hotmix')

listbox.config(height=listbox.size())

submit_button = Button(window, text='submit', command=submit)
submit_button.pack()

window.mainloop()