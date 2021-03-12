from tkinter import *
from send_message import send_message

root = Tk()

root.title('Chat Session')
root.geometry('400x500')
root.resizable(width=False, height=False)

chat_window = Text(root, bd=1, bg='grey', width=50, height=8,
                   font=('Arial', 23), foreground='black')
chat_window.place(x=6, y=6, height=385, width=370)
chat_window.configure(cursor='arrow', state=DISABLED)

scrollbar = Scrollbar(root, command=chat_window.yview, cursor="arrow")
scrollbar.place(x=375, y=5, height=385)

message_window = Text(root, bd=0, bg="grey", width="30", height="4", font=("Arial", 20), foreground="black")
message_window.place(x=140, y=400, height=88, width=260)

Button = Button(root, text="Send", width="12", height=5,
                bd=0, bg="#0080ff", activebackground="#00bfff", foreground='#ffffff', font=("Arial", 12))
Button.place(x=6, y=400, height=88)



def insert_message(msg, sender):
    if not msg:
        return
    msg_entry.delete(0, END)
    msg1 = f"{sender}: {msg}"
    chat_window.configure(state=NORMAL)
    chat_window.insert(END, msg1)
    chat_window.configure(state=DISABLED)



def on_enter_pressed(event):
    msg = msg_entry.get()
    insert_message(msg, 'You')


msg_entry = Entry(message_window, bg='grey', foreground='black', font='Arial, 23')
msg_entry.place(x=0.74, y=0.06, height=0.008, width=0.011)
msg_entry.focus()
msg_entry.bind('<Return>', on_enter_pressed)

root.mainloop()
