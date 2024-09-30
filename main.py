from tkinter import *

# count = 0
# def click():
#     global count
#     count+=1
#     print(count)

# def submit():
#     user = entry.get()
#     print('Hello '+user)

food = ['burger','pizza','pastel','meal']

def order():
    if (x.get() == 0):
        print('you ordered a hamburger')
    elif (x.get() == 1):
        print('you ordered a pizza')
    elif (x.get() == 2):
        print('you ordered a pastel')
    elif (x.get() == 3):
        print('you ordered a meal')
    else:
        print('huh?')

window = Tk()
window.title('XL')
icon = PhotoImage(file='favicon.png')
window.iconphoto(True, icon)

img_burg = PhotoImage(file='burger.png')
img_pizza = PhotoImage(file='pizza.png')
img_pastel = PhotoImage(file='pastel.png')
img_meal = PhotoImage(file='meal.png')
img_list = [img_burg, img_pizza,img_pastel,img_meal]



# entry = Entry(window, font=("Arial",50))
# entry.pack(side=LEFT)
#
# btn_submit = Button(window, text='SUBMIT', command=submit)
# btn_submit.pack(side=RIGHT)

# #window.geometry('800x600')
# #window.config(background='black')

# photo = PhotoImage(file='192x192.png')
# label = Label(window,
#               text='Hello World ☺',
#               font=('Arial',40,'bold'),
#               fg='#f80',
#               bg='#000',
#               relief=RAISED,
#               bd=10,
#               padx=20,
#               pady=20,
#               image=photo,
#               compound='bottom'
#               )
# label.pack()
# #label.place(x=0,y=0)

# img_btn = PhotoImage(file='like.png')
# button = Button(window, text='click me',
#                 command=click,
#                 font=('Comic Sans', 30),
#                 fg='#f80',
#                 bg='#000',
#                 activeforeground='#08f',
#                 activebackground='#fff',
#                 image=img_btn,
#                 compound='bottom')
# button.pack()

x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index], #adds text to radio buttons
                              variable=x, #groups radiobuttons togheter if the share the same variable
                              value=index, #assigns each button a different value
                              padx= 25, #adds padding on x-axis
                              font=('comic sans ms', 36),
                              image = img_list[index],
                              compound='left', #adds img n text (left)
                              indicatoron=FALSE, #deletes the bullets
                              width=375,
                              command=order #set command of radiobutton to function

                              )
    radiobutton.pack(anchor=W)

window.mainloop()