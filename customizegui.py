from tkMessageBox   import showinfo
from tkinter_class import MyGui
class CustomGui(MyGui):
    def __init__(self,msg):
        MyGui.__init__(self)
        self.msg = msg
      
      
    def reply(self):
       
        showinfo(title=self.__str__(),message=self.msg)


if __name__ == '__main__':
    gui = CustomGui('I love the anointed geek')
    gui.pack()
    gui.mainloop()
