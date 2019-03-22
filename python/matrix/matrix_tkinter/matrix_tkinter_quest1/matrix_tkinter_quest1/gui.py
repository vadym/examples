print("DEBUG: Module 'gui.py' is executing")

import logging

#from matrix_tkinter_quest1.core import loggerConfigure

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
    quests = [
        {'beginRow': 0, 'beginCol': 0},
        {'beginRow': 4, 'beginCol': 3},
        {'beginRow': 2, 'beginCol': 4},
        {'beginRow': 4, 'beginCol': 4}
    ]
    questChosen = 0
    questMap = [
        # Row 0
        [
            {'current': 'S', 'next': {'row': 2, 'col': 1}},   # Col 0-0
            {'current': 'A', 'next': {'row': 1, 'col': 4}},   # Col 1-3
            {'current': 'E', 'next': {'row': -1, 'col': -1}}, # Col 2-2
            {'current': 'E', 'next': {'row': 3, 'col': 0}},   # Col 3-0
            {'current': 'A', 'next': {'row': 1, 'col': 0}}    # Col 4-1
        ],

        # Row 1
        [
            {'current': 'U', 'next': {'row': 4, 'col': 0}},   # Col 0-1
            {'current': 'I', 'next': {'row': 3, 'col': 3}},   # Col 1-2
            {'current': 'C', 'next': {'row': 1, 'col': 3}},   # Col 2-0
            {'current': 'C', 'next': {'row': 0, 'col': 3}},   # Col 3-0
            {'current': 'N', 'next': {'row': 4, 'col': 2}}    # Col 4-3
        ],

        # Row 2
        [
            {'current': 'N', 'next': {'row': 1, 'col': 1}},   # Col 0-2
            {'current': 'U', 'next': {'row': 1, 'col': 2}},   # Col 1-0
            {'current': 'U', 'next': {'row': 0, 'col': 2}},   # Col 2-2
            {'current': 'E', 'next': {'row': 0, 'col': 4}},   # Col 3-1
            {'current': 'U', 'next': {'row': 2, 'col': 0}}    # Col 4-2
        ],

        # Row 3
        [
            {'current': 'S', 'next': {'row': 3, 'col': 2}},   # Col 0-0
            {'current': 'H', 'next': {'row': 0, 'col': 1}},   # Col 1-3
            {'current': 'S', 'next': {'row': -1, 'col': -1}}, # Col 2-0
            {'current': 'Q', 'next': {'row': 2, 'col': 2}},   # Col 3-2
            {'current': 'E', 'next': {'row': -1, 'col': -1}}  # Col 4-3
        ],

        # Row 4
        [
            {'current': 'T', 'next': {'row': 4, 'col': 1}},   # Col 0-1
            {'current': 'Y', 'next': {'row': -1, 'col': -1}}, # Col 1-1
            {'current': 'C', 'next': {'row': 3, 'col': 4}},   # Col 2-3
            {'current': 'B', 'next': {'row': 2, 'col': 3}},   # Col 3-1
            {'current': 'C', 'next': {'row': 3, 'col': 1}}    # Col 4-3
        ]
    ]
    

    MAIN_WINDOW_GEOMETRY = '400x573'

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
    quest = tk.StringVar()

    def ChooseQuestCallback(self, event):
        index = self.quest.get()
        self.status.set('Chosen the quest %s' % index)
        self.questChosen = int(index)-1

        self.ChooseQuest()

        for row, rowList in enumerate(self.MatrixWidgets):
            for col, columnList in enumerate(rowList):
                guiCell = self.MatrixWidgets[row][col]
                guiCell_cellWidget = guiCell['cellWidget']

                guiCell_cellWidget.configure(bg='white')

    def ChooseQuest(self):
        quests = self.quests[self.questChosen]
        beginRow = quests['beginRow']
        beginCol = quests['beginCol']

        return self.markQuestRecursive(beginRow, beginCol)

    def markQuestRecursive(self, nextRow, nextCol):
        cell = self.questMap[nextRow][nextCol]
        # Mark this cess as belongs to the quest (by its index)
        cell['questIndex'] = self.questChosen

        nextRow = cell['next']['row']
        nextCol = cell['next']['col']

        if nextRow != -1 and \
           nextCol != -1:
            return self.markQuestRecursive(nextRow, nextCol)

        return 0

    def showWinnerMessage(self):
        tkmbox.showinfo(title='Hurrah. You are winner!',
                        message="You've win after the {} tries and used the {} hints".format(
                            self.quests[self.questChosen].get('checks'), self.quests[self.questChosen].get('hints')
                        ))

    def hintQuestRecursive(self, nextRow, nextCol, error_color, warning_color, success_color):
        questCell = self.questMap[nextRow][nextCol]

        guiCell = self.MatrixWidgets[nextRow][nextCol]
        guiCell_cellWidget = guiCell['cellWidget']
        guiCell_cellString = guiCell['cellString']

        cellText = guiCell_cellString.get()

        if   cellText == '':
            guiCell_cellWidget.configure(bg=warning_color)
            return -1

        elif cellText != questCell['current']:
            guiCell_cellWidget.configure(bg=error_color)
            return -1

        else:
            guiCell_cellWidget.configure(bg=success_color)

        nextRow = questCell['next']['row']
        nextCol = questCell['next']['col']

        if nextRow != -1 and \
           nextCol != -1:
            return self.hintQuestRecursive(nextRow, nextCol, error_color, warning_color, success_color)

        self.showWinnerMessage()
        return 0

#    def BeginsCallback(self):
#        for index, begin in enumerate(self.quests):
#            beginRow = begin['row']
#            beginCol = begin['col']
#
#            try:
#                guiCell = self.MatrixWidgets[beginRow][beginCol]
#                guiCell_cellWidget = guiCell['cellWidget']
#                guiCell_cellString = guiCell['cellString']
#
#                guiCell_cellWidget.configure(bg='deep sky blue')
#            except IndexError:
#                tkmbox.showinfo(title='Error: Quest begin point',
#                                message="Quest with index '{}' can't begin from the point: row '{}', col '{}'".format(
#                                    index,
#                                    beginRow,
#                                    beginCol
#                                ))

    def HintCallback(self):
        hints = self.quests[ self.questChosen ].get('hints', 0) + 1
        self.quests[ self.questChosen ]['hints'] = hints

        self.status.set('Hint number %s' % hints)

        self.Hint()

    def Hint(self):
        row = self.quests[ self.questChosen ]['beginRow']
        col = self.quests[ self.questChosen ]['beginCol']

        self.hintQuestRecursive(row, col, 'red', 'yellow', 'light green')

    def CheckCallback(self):
        checks = self.quests[ self.questChosen ].get('checks', 0) + 1
        self.quests[ self.questChosen ]['checks'] = checks

        self.status.set('Check number %s' % checks)

        self.Check()

    def Check(self):
        for row, rowList in enumerate(self.MatrixWidgets):
            for col, columnList in enumerate(rowList):
                guiCell = self.MatrixWidgets[row][col]
                guiCell_cellWidget = guiCell['cellWidget']
                guiCell_cellString = guiCell['cellString']

                # Check if you provide a letter...
                guiCell_text = guiCell_cellString.get()
                # .. and comparing with the quest array.
                questCell = self.questMap[row][col]

                questIndex = questCell.get('questIndex')
                if questIndex is not None and \
                   questIndex == self.questChosen:
                    # Seems, something must be set here.
                    if questCell['current'] != guiCell_cellString.get():
                        # Wrong letter
                        guiCell_cellWidget.configure(bg='red')
                        tkmbox.showinfo(title="Mistake",
                                        message="You've made a mistake: Letter '{}'. Use another one.".format(
                                            guiCell_text
                                        ))
                        guiCell_cellString.set('')
                        guiCell_cellWidget.configure(bg='white')
                    else:
                        # Correct letter
                        guiCell_cellWidget.configure(bg='light green')

# Just ignore this case because this is not an error.
#                    else:
#                        # Cell does not belong to this quest.
#                        guiCell_cellWidget.configure(bg='red')
#                        tkmbox.showinfo(title="Mistake",
#                                        message="You've made a mistake: Letter '{}'. Cell does not belong to this quest.".format(
#                                            guiCell_text
#                                        ))
#                        guiCell_cellString.set('')
#                        guiCell_cellWidget.configure(bg='white')

    def __init__(self):
        self.ChooseQuest()

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

        self.MiddleFrameWidget_Right.grid(column=3, row=0, pady=10, padx=2, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Bottom Widget
        self.BottomFrameWidget.grid_columnconfigure(0, weight=3, pad=3)
        self.BottomFrameWidget.grid(column=0, row=2, sticky=(tk.W, tk.E, tk.N, tk.S))

        ##
        # Top Widget fulfilling
        #

        # Top Widget: Row 1
        label_actions = tk.Label(self.TopFrameWidget, text="Choose quest")
        label_actions.grid(column=0, row=0, sticky=tk.E)

        quest = ttk.Combobox(self.TopFrameWidget, width=20, textvariable=self.quest,
                             values=[i+1 for i, _ in enumerate(self.quests)])
        quest.grid(column=1, row=0, sticky=(tk.W, tk.E))
        quest.current(0)
        quest.bind("<<ComboboxSelected>>", self.ChooseQuestCallback)

        #button_begins = tk.Button(self.TopFrameWidget, text='Begins', command=self.BeginsCallback)
        #button_begins.grid(column=2, row=0, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))

        button_hint = tk.Button(self.TopFrameWidget, text='Hint', command=self.HintCallback)
        button_hint.grid(column=2, row=0, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))

        button_check = tk.Button(self.TopFrameWidget, text='Check', command=self.CheckCallback)
        button_check.grid(column=3, row=0, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))

        ##
        # Middle Widget fulfilling
        #
        rowList = list()
        for row in range(len(self.questMap)): # 4

            colList = list()
            for col in range(len(self.questMap[0])): # 4

                cellString = tk.StringVar()
                cellWidget = tk.Entry(self.MiddleFrameWidget_CenterLeft, width=3, textvariable=cellString)
                cellWidget.grid(column=col, row=row, padx=2, pady=2, sticky=(tk.W, tk.E, tk.N, tk.S))

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

        ##
        # Bottom Widget fulfilling
        #
        statusWidget = tk.Label(self.BottomFrameWidget, text="Started", textvariable=self.status,
                                     bd=1, relief=tk.SUNKEN, anchor=tk.W)
        statusWidget.grid(column=0, row=4, padx=2, sticky=(tk.W, tk.E))

        self.windowWidget.mainloop()
