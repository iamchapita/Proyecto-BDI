from tkinter import *

class ScreenCenter:

    def center(self, parent):                
        width = parent.winfo_reqwidth()
        height =parent.winfo_reqheight()
        print("Width", parent.winfo_screenwidth(), "Height", parent.winfo_screenheight())
        positionRight = int(parent.winfo_screenwidth()/2 - width + 50)
        positionDown = int(parent.winfo_screenheight()/2 - height)
        print(positionRight, positionDown)
        # Positions the window in the center of the page.
        parent.geometry("+{}+{}".format(positionRight, positionDown))
