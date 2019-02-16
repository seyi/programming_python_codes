from Tkinter import *
from tkMessageBox import showinfo

class MyGui(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        button = Button(self,text='press me',command=self.reply)
        button.pack()
    def reply(self):
        showinfo(title='Greetings',message='Hello anointed geek')

if __name__ == '__main__':
    window = MyGui()
    window.pack()
    window.mainloop()