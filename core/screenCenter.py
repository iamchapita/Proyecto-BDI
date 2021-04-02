from tkinter import *

class ScreenCenter:

    def center(self, parent, width, height):
        xCoordinate = int(parent.winfo_screenwidth()/2 - width/2)
        yCoordinate = int(parent.winfo_screenheight()/2 - height/2)
        parent.geometry('%dx%d+%d+%d' % (width, height, xCoordinate, yCoordinate))