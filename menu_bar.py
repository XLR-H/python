from tkinter import *


def open_file():
    print("file has been opened")


def save_file():
    print('file has been saved')


window = Tk()
window.title('XL')
icon = PhotoImage(file='img\\favicon.png')
window.iconphoto(True, icon)
window.geometry('400x300')
window.config(background='black')


img_new = PhotoImage(file='img\\a_file.png')
img_open = PhotoImage(file='img\\a_folder.png')
img_save = PhotoImage(file='img\\a_save.png')
img_exit = PhotoImage(file='img\\a_exit.png')
img_cut = PhotoImage(file='img\\a_cut.png')
img_copy = PhotoImage(file='img\\a_copy.png')
img_paste = PhotoImage(file='img\\a_paste.png')

menubar = Menu(window)
window.config(menu=menubar)

file_menu = Menu(menubar,tearoff=0,font=('Helvetica',12))
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New",image=img_new,compound='left')
file_menu.add_command(label="Open",command=open_file,image=img_open,compound='left')
file_menu.add_command(label="Save",command=save_file,image=img_save,compound='left')
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit, image=img_exit,compound='left')


edit_menu = Menu(menubar, tearoff=0,font=('Helvetica',12))
menubar.add_cascade(label='Edit',menu=edit_menu)
edit_menu.add_command(label="Cut",command=open_file,image=img_cut,compound='left')
edit_menu.add_command(label="Copy",command=open_file,image=img_copy,compound='left')
edit_menu.add_command(label="Paste",command=open_file,image=img_paste,compound='left')







window.mainloop()
