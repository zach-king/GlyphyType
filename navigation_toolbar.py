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
        self.prevButton = QPushButton('Prev')
        self.currentGlyphDisplay = QLabel('Current Glyph')
        self.currentGlyphDisplay.setAlignment(Qt.AlignCenter)
        self.nextButton = QPushButton('Next')

        # Add the buttons to a layout for self
        layout = QHBoxLayout()
        layout.addWidget(self.prevButton)
        layout.addWidget(self.currentGlyphDisplay)
        layout.addWidget(self.nextButton)

        # Set the layout
        self.setLayout(layout)