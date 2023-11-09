from tkinter import *


# def say_hello():
#     name_of_user = entry_1.get()
#     string_to_display = 'Hello ' + name_of_user
#     label_2 = Label(my_window)
#     label_2['text'] = string_to_display
#     label_2.grid(row=1, column=1)


my_window = Tk()
#
# label_1 = Label(my_window,
#                 text='Please enter your name:')
# entry_1 = Entry(my_window)
# button_1 = Button(my_window,
#                   text='Click me to enter name',
#                   command=say_hello)
#
# label_1.grid(row=0, column=0)
# entry_1.grid(row=0, column=1)
# button_1.grid(row=1, column=0)


# 29. THE ENTRY WIDGET AND STRINGVAR
def say_hello():
    # name_of_user = var_2.get()
    # var_1.set('Hello ' + name_of_user)
    var_1.set('Hello ' + var_2.get())


var_1 = StringVar()
var_2 = StringVar()

label_1 = Label(my_window,
                text='Please enter your name:')
entry_1 = Entry(my_window, textvariable=var_2)
button_1 = Button(my_window,
                  text='Click me to enter name',
                  command=say_hello)
label_2 = Label(my_window,
                textvariable=var_1)

label_1.grid(row=0, column=0)
entry_1.grid(row=0, column=1)
button_1.grid(row=1, column=0)
label_2.grid(row=1, column=1)

my_window.mainloop()
