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
        self.mainMenuBar = self.menuBar()
        self.fileMenu = QMenu('&File')
        self.fileMenu.addAction('&New Font', self.newFont, 'Ctrl+N')
        self.fileMenu.addAction('&New Glyph', self.newGlyph, 'Ctrl+Shift+N')
        self.fileMenu.addSeparator()
        self.fileMenu.addAction('&Import Font', self.importFont, 'Ctrl+O')
        self.fileMenu.addAction('&Export Font', self.exportFont, 'Ctrl+S')
        self.fileMenu.addSeparator()
        self.fileMenu.addAction('E&xit', self.quit, 'Ctrl+Q')
        self.mainMenuBar.addMenu(self.fileMenu)

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

    def newFont(self):
        '''Menu command for constructing a new font.'''
        pass

    def newGlyph(self):
        '''Menu command for constructing a new individual glyph.'''
        pass

    def importFont(self):
        '''Menu command for importing a GlyphyType font.'''
        pass

    def exportFont(self):
        '''Menu command for exporting a GlyphyType font.'''
        pass

    def quit(self):
        pass





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GlyphyApp()
    window.show()
    sys.exit(app.exec_())