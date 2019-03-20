print("DEBUG: Module 'gui.py' is executing")

import logging

#from matrix_tkinter_guess_next_4x4.core import loggerConfigure

import tkinter as tk
from tkinter import ttk
#from tkinter import messagebox as tkmbox

#import pkg_resources
#
#filename = "gui.py"
#filepath = pkg_resources.resource_filename(__name__, filename)
#print("DEBUG: Path: %s (__name__: %s)" % (filepath, __name__))


class Gui:
    questMap = [
        # Row 1
        [
            # Cell 1
            {'next': {'row': 2, 'col': 1}, 'current': 'S'}, # <-- Start HERE
            # Cell 2
            None,
            # Cell 3
            None,
            # Cell 4
            {'next': {'row': 3, 'col': 0}, 'current': 'E'}
        ],

        # Row 2
        [
            # Cell 1
            None,
            # Cell 2
            None,
            # Cell 3
            {'next': {'row': 1, 'col': 3}, 'current': 'C'},
            # Cell 4
            {'next': {'row': 0, 'col': 3}, 'current': 'C'}
        ],

        # Row 3
        [
            # Cell 1
            None,
            # Cell 2
            {'next': {'row': 1, 'col': 2}, 'current': 'U'},
            # Cell 3
            None,
            # Cell 4
            None
        ],

        # Row 4
        [
            # Cell 1
            {'next': {'row': 3, 'col': 2}, 'current': 'S'},
            # Cell 2
            None,
            # Cell 3
            {'next': {'row': None, 'col': None}, 'current': 'S'},
            # Cell 4
            None
        ]
    ]

    MAIN_WINDOW_GEOMETRY = '140x193'

    # Main window widget
    windowWidget = tk.Tk()

    # Window Layout widgets
    TopFrameWidget = tk.Frame()
    MiddleFrameWidget = tk.Frame()
    BottomFrameWidget = tk.Frame()

    LeftFrameWidget = tk.Frame(MiddleFrameWidget)
    LeftFrameWidget.grid(column=0, row=0, pady=10, padx=2, sticky=(tk.W, tk.E, tk.N, tk.S))

    MatrixFrameWidget = tk.Frame(MiddleFrameWidget)
    MatrixFrameWidget.grid(column=1, row=0, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

    MatrixFrameWidgets = list()

    RightFrameWidget = tk.Frame(MiddleFrameWidget)
    RightFrameWidget.grid(column=2, row=0, pady=10, padx=2, sticky=(tk.W, tk.E, tk.N, tk.S))

    status = tk.StringVar()
    #color = tk.StringVar()

    checks = 0
    hints = 0

#    colors = ['white', 'red', 'orange', 'yellow', 'green', 'deep sky blue', 'blue', 'violet', 'black']

#    def ComboCallback(self, event):
#        self.status.set('Change color to %s' % self.color.get())
#        self.Update()

#    def Update(self):
#        for label in self.MatrixFrameWidgets:
#            label.configure(bg=self.color.get())

    def HintCallback(self):
        self.status.set('Hint number %s' % self.hints)
        self.hints += 1

        self.Hint()

    def Hint(self):
        # TODO: Put to a function because of duplication
        questCell = self.questMap[0][0]

        guiCell = self.MatrixFrameWidgets[0][0]
        guiCell_cellWidget = guiCell['cellWidget']
        guiCell_cellString = guiCell['cellString']

        if questCell['current'] != guiCell_cellString.get():
            guiCell_cellWidget.configure(bg='yellow')
            return -1
        else:
            guiCell_cellWidget.configure(bg='light green')

        nextRow = questCell['next']['row']
        nextCol = questCell['next']['col']

        while nextRow is not None and \
              nextCol is not None:

            # TODO: Put to a function because of duplication
            questCell = self.questMap[nextRow][nextCol]

            guiCell = self.MatrixFrameWidgets[nextRow][nextCol]
            guiCell_cellWidget = guiCell['cellWidget']
            guiCell_cellString = guiCell['cellString']

            if questCell['current'] != guiCell_cellString.get():
                guiCell_cellWidget.configure(bg='yellow')
                break
            else:
                guiCell_cellWidget.configure(bg='green')

            nextRow = questCell['next']['row']
            nextCol = questCell['next']['col']

        else:
            return 0

        return -1

    def CheckCallback(self):
        self.status.set('Check number %s' % self.checks)
        self.checks += 1

        self.Check()

    def Check(self):
        for row, rowList in enumerate(self.MatrixFrameWidgets):
            for col, columnList in enumerate(rowList):
                guiCell = self.MatrixFrameWidgets[row][col]
                guiCell_cellWidget = guiCell['cellWidget']
                guiCell_cellString = guiCell['cellString']

                questCell = self.questMap[row][col]
                if questCell is not None:
                    if questCell['current'] != guiCell_cellString.get():
                        guiCell_cellWidget.configure(bg='red')

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
        label_actions = tk.Label(self.TopFrameWidget, text="Actions")
        label_actions.grid(column=0, row=0, sticky=tk.E)

        button_hint = tk.Button(self.TopFrameWidget, text='Hint', command=self.HintCallback)
        button_hint.grid(column=1, row=0, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))

        button_check = tk.Button(self.TopFrameWidget, text='Check', command=self.CheckCallback)
        button_check.grid(column=2, row=0, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))

#        combo = ttk.Combobox(self.TopFrameWidget, width=20, textvariable=self.color,
#                             values=self.colors)
#        combo.grid(column=1, row=0, sticky=(tk.W, tk.E))
#        combo.current(0)
#        combo.bind("<<ComboboxSelected>>", self.ComboCallback)

        ##
        # Middle Widget fulfilling
        #
        rowList = list()
        for row in range(4):

            colList = list()
            for col in range(4):

                cellString = tk.StringVar()
                cellWidget = tk.Entry(self.MatrixFrameWidget, width=3, textvariable=cellString)
                cellWidget.grid(column=col, row=row, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))

                cell = {
                    'cellWidget': cellWidget,
                    'cellString': cellString
                }
                colList.append(cell)

            rowList.append(colList)

        # Save widgets to access to the matrix cells
        self.MatrixFrameWidgets = rowList

##
# Case 2
#

#                label = tk.Label(self.MiddleFrameWidget, text=str(row + 1) + 'x' + str(column + 1),
#                           width=4, height=2, bg=self.colors[0])
#                label.grid(column=column, row=row, padx=2, pady=2, sticky=(tk.W, tk.E, tk.N, tk.S))
#
#                # Save widgets to access to the matrix cells
#                #index = row * 8 + column
#                self.MatrixFrameWidgets.append(label)

##
# Case 1
#

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
