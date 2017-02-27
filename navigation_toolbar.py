'''
File:       navigation_toolbar.py
Description: 
            Implements the NavigationToolbar class which encapsulates the
            nav buttons for GlyphType. This widget is not exactly a 
            "toolbar" as defined by Qt, but has the functionality and 
            appearance of a toolbar. 
'''

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class NavigationToolbar(QFrame):
    def __init__(self, parent=None):
        super(NavigationToolbar, self).__init__(parent)

        # Build the tool buttons
        self.buildWidgets()

    def buildWidgets(self):
        # Create the Push Buttons
        self.prevButton = QToolButton()
        self.prevButton.setIcon(QIcon('./config/icons/prev-icon.png'))
        self.prevButton.setText('Prev')
        self.prevButton.setFixedWidth(400)
        self.prevButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.currentGlyphDisplay = QLabel('Current Glyph')
        self.currentGlyphDisplay.setAlignment(Qt.AlignCenter)
        self.nextButton = QToolButton()
        self.nextButton.setText('Next')
        self.nextButton.setFixedWidth(400)
        self.nextButton.setIcon(QIcon('./config/icons/next-icon.png'))
        self.nextButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        # Add the buttons to a layout for self
        layout = QHBoxLayout()
        layout.addWidget(self.prevButton)
        layout.addWidget(self.currentGlyphDisplay)
        layout.addWidget(self.nextButton)

        # Set the layout
        self.setLayout(layout)