import tkinter as tk
from ChatBot import *


root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Cal the SQRT')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 30, window=label1)

label2 = tk.Label(root, text='Type num')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry(send_message)
canvas1.create_window(200, 140, window=entry1)


def get_sqrt():

    x1 = entry1.get()

    label3 = tk.Label(root, text= 'the sqrt of '+x1+' is:', font=('helvetica', 10))
    canvas1.create_window(200, 210, window=label3)
    label4 = tk.Label(root, text= float(x1)**0.5, font=('helvetica', 10, 'bold'))
    canvas1.create_window(200, 230, window=label4)


button1 = tk.Button(text='get the sqrt', command=get_sqrt, bg='brown')
canvas1.create_window(200, 180, window=button1)

root.mainloop()
