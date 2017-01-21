'''
File:       utility_toolbar.py
Description: 
            Implements the UtilityToolbar class which encapsulates the
            tools buttons for GlyphType. This widget is not exactly a 
            "toolbar" as defined by Qt, but has the functionality and 
            appearance of a toolbar. 
'''

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class UtilityToolbar(QFrame):
    def __init__(self, parent=None):
        super(UtilityToolbar, self).__init__(parent)

        # Build the tool buttons
        self.buildWidgets()

    def buildWidgets(self):
        # Create the Push Buttons
        self.brushButton = QPushButton('Brush')
        self.lineButton = QPushButton('Line')
        self.shapeButton = QPushButton('Shape')
        self.eraserButton = QPushButton('Eraser')
        self.toggleReferenceButton = QPushButton('Toggle Reference')
        self.fillButton = QPushButton('Color Fill')
        self.exportButton = QPushButton('Export')
        self.clearButton = QPushButton('CLEAR ALL')

        # Add the buttons to a layout for self
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.brushButton)
        buttonLayout.addWidget(self.lineButton)
        buttonLayout.addWidget(self.shapeButton)
        buttonLayout.addWidget(self.eraserButton)
        buttonLayout.addWidget(self.toggleReferenceButton)
        buttonLayout.addWidget(self.fillButton)
        buttonLayout.addWidget(self.exportButton)
        buttonLayout.addWidget(self.clearButton)

        # Set the layout
        self.setLayout(buttonLayout)