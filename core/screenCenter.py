from tkinter import *

class ScreenCenter:

    def center(self, parent, width, height):
        positionRight = int((parent.winfo_screenwidth()/2) - (width/2))
        positionDown = int((parent.winfo_screenheight()/2) - (height/2))
        parent.geometry("+{}+{}".format(positionRight, positionDown))
