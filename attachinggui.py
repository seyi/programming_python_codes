from Tkinter import *
from tkinter_class import MyGui

# Main app window
mainwin = Tk()
Label(mainwin,text=__name__).pack()

# Pop up window
popup = Toplevel()
Label(popup,text='Attach').pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)
mainwin.mainloop()