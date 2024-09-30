from tkinter import *
from tkinter import filedialog

# def open_file():
#     filepath = filedialog.askopenfilename(initialdir='E:\\Rafael\\code\\python\\window',
#                                           title='Open File:',
#                                           filetypes= (('Text Files','*.txt'),('all files','*.*')
#                                           ))
#     file = open(filepath,'r')
#     print(file.read())
#     file.close()


def save_file():
    file = filedialog.asksaveasfile(defaultextension='.txt',filetypes=[('text file','.txt'),
                                                                       ('HTML file','.html'),
                                                                       ('All files','.*')
                                                                       ])
    file_text = str(text.get(1.0, END))
    file.write(file_text)
    file.close()


window = Tk()
window.title('XL')
icon = PhotoImage(file='favicon.png')
window.iconphoto(True, icon)
window.geometry('400x300')
window.config(background='black')


button = Button(text='save', command=save_file)
button.pack()
text = Text(window)
text.pack()

window.mainloop()