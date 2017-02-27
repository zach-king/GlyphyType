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
        self.app = parent

        # Build the tool buttons
        self.buildWidgets()

    def buildWidgets(self):
        # Create the Push Buttons
        self.brushButton = QPushButton('Brush')
        self.brushButton.setIcon(QIcon('./config/icons/brush-icon.png'))
        self.brushButton.clicked.connect(self.app.selectBrushTool)
        self.lineButton = QPushButton('Line')
        self.lineButton.setIcon(QIcon('./config/icons/line-icon.png'))
        self.lineButton.clicked.connect(self.app.selectLineTool)
        self.rectangleButton = QPushButton('Rectangle')
        self.rectangleButton.setIcon(QIcon('./config/icons/rectangle-icon.png'))
        self.rectangleButton.clicked.connect(self.app.selectRectangleTool)
        self.eraserButton = QPushButton('Eraser')
        self.eraserButton.setIcon(QIcon('./config/icons/eraser-icon.png'))
        self.toggleReferenceButton = QPushButton('Toggle Reference')
        self.toggleReferenceButton.setIcon(QIcon('./config/icons/reference-icon.png'))
        self.fillButton = QPushButton('Color Fill')
        self.fillButton.setIcon(QIcon('./config/icons/fill-icon.png'))
        self.exportButton = QPushButton('Export')
        self.exportButton.setIcon(QIcon('./config/icons/export-icon.png'))
        self.clearButton = QPushButton('CLEAR ALL')
        self.clearButton.setIcon(QIcon('./config/icons/clear-icon.png'))
        self.clearButton.clicked.connect(self.app.clearCanvas)

        # Add the buttons to a layout for self
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.brushButton)
        buttonLayout.addWidget(self.lineButton)
        buttonLayout.addWidget(self.rectangleButton)
        buttonLayout.addWidget(self.eraserButton)
        buttonLayout.addWidget(self.toggleReferenceButton)
        buttonLayout.addWidget(self.fillButton)
        buttonLayout.addWidget(self.exportButton)
        buttonLayout.addWidget(self.clearButton)

        # Set the layout
        self.setLayout(buttonLayout)