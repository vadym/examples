print("DEBUG: Module 'gui.py' is executing")

import logging

#from matrix_tkinter_guess_next_4x4.core import loggerConfigure

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as tkmbox

#import pkg_resources
#
#filename = "gui.py"
#filepath = pkg_resources.resource_filename(__name__, filename)
#print("DEBUG: Path: %s (__name__: %s)" % (filepath, __name__))

import json


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
    

    MAIN_WINDOW_GEOMETRY = '393x573'

    # Main window widget
    windowWidget = tk.Tk()

    # Window Layout widgets
    TopFrameWidget = tk.Frame(windowWidget)
    MiddleFrameWidget = tk.Frame(windowWidget)
    BottomFrameWidget = tk.Frame(windowWidget)

    MiddleFrameWidget_Left = tk.Frame(MiddleFrameWidget)
    MiddleFrameWidget_CenterLeft = tk.Frame(MiddleFrameWidget)
    MiddleFrameWidget_CenterRight = tk.Frame(MiddleFrameWidget) # , width=300, height=600
    MiddleFrameWidget_Right = tk.Frame(MiddleFrameWidget)

    MatrixWidgets = list()

    status = tk.StringVar()
    #color = tk.StringVar()

    checks = 0
    hints = 0

#    colors = ['white', 'red', 'orange', 'yellow', 'green', 'deep sky blue', 'blue', 'violet', 'black']

#    def ComboCallback(self, event):
#        self.status.set('Change color to %s' % self.color.get())
#        self.Update()

#    def Update(self):
#        for label in self.MatrixWidgets:
#            label.configure(bg=self.color.get())

    def showWinnerMessage(self):
        tkmbox.showinfo(title='Hurrah. You are winner!',
                        message="You've win after the {} tries and used the {} hints".format(
                            self.checks, self.hints
                        ))

    def walkThroughAllTrack(self, nextRow, nextCol):
        questCell = self.questMap[nextRow][nextCol]

        guiCell = self.MatrixWidgets[nextRow][nextCol]
        guiCell_cellWidget = guiCell['cellWidget']
        guiCell_cellString = guiCell['cellString']

        if questCell['current'] != guiCell_cellString.get():
            guiCell_cellWidget.configure(bg='yellow')
            return -1
        else:
            guiCell_cellWidget.configure(bg='light green')

        nextRow = questCell['next']['row']
        nextCol = questCell['next']['col']

        if nextRow is not None and \
           nextCol is not None:
            self.walkThroughAllTrack(nextRow, nextCol)
        else:
            self.showWinnerMessage()
            return 0
        return -1

    def HintCallback(self):
        self.hints += 1
        self.status.set('Hint number %s' % self.hints)

        self.Hint()

    def Hint(self):
        return self.walkThroughAllTrack(0, 0)

    def CheckCallback(self):
        self.checks += 1
        self.status.set('Check number %s' % self.checks)

        self.Check()

    def Check(self):
        for row, rowList in enumerate(self.MatrixWidgets):
            for col, columnList in enumerate(rowList):
                guiCell = self.MatrixWidgets[row][col]
                guiCell_cellWidget = guiCell['cellWidget']
                guiCell_cellString = guiCell['cellString']

                # Check if you provide a letter...
                guiCell_text = guiCell_cellString.get()
                if guiCell_text != '':
                    # Oh, you put there something.. Comparing with the quest array..
                    questCell = self.questMap[row][col]
                    if questCell is not None:
                        # Seems, something must be set here.
                        if questCell['current'] != guiCell_cellString.get():
                            # Wrong letter
                            guiCell_cellWidget.configure(bg='red')
                            tkmbox.showinfo(title="Mistake",
                                            message="You've made a mistake: wrong letter {}. Use another one.".format(
                                                guiCell_text
                                            ))
                            guiCell_cellString.set('')
                            guiCell_cellWidget.configure(bg='white')
                        else:
                            # Correct letter
                            guiCell_cellWidget.configure(bg='light green')
                    else:
                        # Cell must be empty.
                        guiCell_cellWidget.configure(bg='red')
                        tkmbox.showinfo(title="Mistake",
                                        message="You made a mistake: wrong letter {}. Cell must be empty.".format(
                                            guiCell_text
                                        ))
                        guiCell_cellString.set('')
                        guiCell_cellWidget.configure(bg='white')

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

        self.MiddleFrameWidget_Left.grid(column=0, row=0, pady=10, padx=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.MiddleFrameWidget_CenterLeft.grid(column=1, row=0, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.MiddleFrameWidget_CenterRight.grid(column=2, row=0, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

        # ensure a consistent GUI size
        #self.MiddleFrameWidget_CenterRight.grid_propagate(False)
        # implement stretchability
        #self.MiddleFrameWidget_CenterRight.grid_rowconfigure(0, weight=1)
        #self.MiddleFrameWidget_CenterRight.grid_columnconfigure(0, weight=1)

        self.MiddleFrameWidget_Right.grid(column=3, row=0, pady=10, padx=2, sticky=(tk.W, tk.E, tk.N, tk.S))

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
                cellWidget = tk.Entry(self.MiddleFrameWidget_CenterLeft, width=3, textvariable=cellString)
                cellWidget.grid(column=col, row=row, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))

                cell = {
                    'cellWidget': cellWidget,
                    'cellString': cellString
                }
                colList.append(cell)

            rowList.append(colList)

        # Save widgets to access to the matrix cells
        self.MatrixWidgets = rowList

        # Show the matrix array
        text = tk.Text(self.MiddleFrameWidget_CenterRight, height=30, width=30)
        text.grid(column=0, row=0, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))
        text.insert(tk.END, json.dumps(self.questMap, indent=4))

        #scroll = tk.Scrollbar(self.MiddleFrameWidget_CenterRight, command=text.yview)
        #scroll.grid(column=2, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        #text['yscrollcommand'] = scroll.set

##
# Case 2
#

#                label = tk.Label(self.MiddleFrameWidget, text=str(row + 1) + 'x' + str(column + 1),
#                           width=4, height=2, bg=self.colors[0])
#                label.grid(column=column, row=row, padx=2, pady=2, sticky=(tk.W, tk.E, tk.N, tk.S))
#
#                # Save widgets to access to the matrix cells
#                #index = row * 8 + column
#                self.MatrixWidgets.append(label)

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
