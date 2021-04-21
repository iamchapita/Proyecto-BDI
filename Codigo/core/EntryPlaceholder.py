# -*- coding: utf-8 -*-
from tkinter import *

class EntryPlaceholder:

    def __init__(self, entry, placeholder):
        self.entry = entry
        self.placeholder = placeholder
        self.__putPlaceholder()
        self.entry.bind("<FocusIn>", self.__deletePlaceholder)
        self.entry.bind("<FocusOut>", self.__setPlaceholder)

    def __putPlaceholder(self):
        self.entry.insert(0, self.placeholder)

    def __setPlaceholder(self, event):
        if (not self.entry.get()):
            self.entry.insert(0, self.placeholder)
    
    def __deletePlaceholder(self, event):
        self.entry.delete("0", "end")
