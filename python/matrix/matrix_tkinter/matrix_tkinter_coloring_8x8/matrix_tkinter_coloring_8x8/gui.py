print("DEBUG: Module 'gui.py' is executing")

import logging

#from matrix_tkinter_coloring_8x8.core import loggerConfigure

import tkinter as tk
from tkinter import ttk
#from tkinter import messagebox as tkmbox

#import pkg_resources
#
#filename = "gui.py"
#filepath = pkg_resources.resource_filename(__name__, filename)
#print("DEBUG: Path: %s (__name__: %s)" % (filepath, __name__))


class Gui:
    MAIN_WINDOW_GEOMETRY = '305x365'

    # Main window widget
    windowWidget = tk.Tk()

    # Window Layout widgets
    TopFrameWidget = tk.Frame()
    MiddleFrameWidget = tk.Frame()
    BottomFrameWidget = tk.Frame()

    MiddleFrameWidgetMatrix = list()

    status = tk.StringVar()
    color = tk.StringVar()

    colors = ['white', 'red', 'orange', 'yellow', 'green', 'deep sky blue', 'blue', 'violet', 'black']

    def ComboCallback(self, event):
        self.status.set('Change color to %s' % self.color.get())
        self.Update()

    def Update(self):
        for label in self.MiddleFrameWidgetMatrix:
            label.configure(bg=self.color.get())

    def __init__(self):
        # Main window Widget
        self.windowWidget.grid_columnconfigure(0, weight=3, pad=3)
        self.windowWidget.grid_columnconfigure(1, weight=3, pad=3)
        self.windowWidget.grid_columnconfigure(2, weight=3, pad=3)
        self.windowWidget.geometry(self.MAIN_WINDOW_GEOMETRY)
        self.windowWidget.resizable(False, False)

        # Top Widget
        self.TopFrameWidget.grid_columnconfigure(0, weight=3, pad=3)
        self.TopFrameWidget.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Middle Widget
        self.MiddleFrameWidget.grid_columnconfigure(0, weight=3, pad=3)
        self.MiddleFrameWidget.grid(column=0, row=1, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Bottom Widget
        self.BottomFrameWidget.grid_columnconfigure(0, weight=3, pad=3)
        self.BottomFrameWidget.grid(column=0, row=2, sticky=(tk.W, tk.E, tk.N, tk.S))

        ##
        # Top Widget fulfilling
        #

        # Top Widget: Row 1
        label_color = tk.Label(self.TopFrameWidget, text="Color")
        label_color.grid(column=0, row=0, sticky=tk.E)

        combo = ttk.Combobox(self.TopFrameWidget, width=20, textvariable=self.color,
                             values=self.colors)
        combo.grid(column=1, row=0, sticky=(tk.W, tk.E))
        combo.current(0)
        combo.bind("<<ComboboxSelected>>", self.ComboCallback)

        ##
        # Middle Widget fulfilling
        #
        for row in range(8):
            for column in range(8):
                label = tk.Label(self.MiddleFrameWidget, text=str(row + 1) + 'x' + str(column + 1),
                           width=4, height=2, bg=self.colors[0])
                label.grid(column=column, row=row, padx=2, pady=2, sticky=(tk.W, tk.E, tk.N, tk.S))

                # Save widgets to access to the matrix cells
                index = row * 8 + column
                self.MiddleFrameWidgetMatrix.append(label)

#        tree = ttk.Treeview(self.MiddleFrameWidget)
#        tree.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
#
#        tree['show'] = 'headings'
#        tree['columns'] = [''] + [i+1 for i in range(8)]
#
#        for column in tree['columns']:
#            tree.heading(column, text=column)
#            tree.column(column, width=15)
#
#        for row in range(8):
#            tree.insert('', tk.END, values=row+1)

        ##
        # Bottom Widget fulfilling
        #
        statusWidget = tk.Label(self.BottomFrameWidget, text="Started", textvariable=self.status,
                                     bd=1, relief=tk.SUNKEN, anchor=tk.W)
        statusWidget.grid(column=0, row=4, padx=2, sticky=(tk.W, tk.E))

        self.windowWidget.mainloop()
