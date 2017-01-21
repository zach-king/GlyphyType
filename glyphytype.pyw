'''
File:       glyphytype.pwy
Description: 
            This is the primary application file for the GlyphyType 
            application. The GlyphyApp class implemented here is 
            a Qt Main Window, which acts as the main window for the app.
            
            Note: this file has a .pyw extension which tells Python 
            it is a GUI program, so if ran, it will not pop up 
            with the console window as well as the GUI window--an idea
            specification for a GUI application.
'''

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

class GlyphyApp(QMainWindow):
    '''Top-level Application for GlyphyType app'''
    def __init__(self, parent=None):
        super(GlyphyApp, self).__init__(parent)

        # Application metadata
        self.appTitle = 'GlyphyType'

        # Build the UI
        self.buildWidgets()

    def buildWidgets(self):
        '''Constructs the user interface for the app'''
        # Build the Main toolbar
        self.buildMainToolbar()

        # Build the Utility Toolbar
        self.buildUtilityToolbar()

        # Build the canvas
        self.buildCanvas()

        # Build the Navigation Toolbar
        self.buildNavigationToolbar()

    def buildMainToolbar(self):
        '''Constructs the main app toolbar (File, Edit, Help, etc.)'''
        pass

    def buildUtilityToolbar(self):
        '''Constructs the Utility Toolbar with drawing tools, etc.'''
        pass

    def buildCanvas(self):
        '''Constructs the drawing canvas for the user to draw glyphs on.'''
        pass

    def buildNavigationToolbar(self):
        '''Constructs the Navigation Toolbar for the user
        to move to next/previous glyphs, and show/hide reference.'''
        pass





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GlyphyApp()
    window.show()
    sys.exit(app.exec_())