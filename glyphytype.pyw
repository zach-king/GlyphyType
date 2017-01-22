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

from utility_toolbar import UtilityToolbar
from navigation_toolbar import NavigationToolbar
from canvas import Canvas


class Container(QWidget):
    def __init__(self, parent=None):
        super(Container, self).__init__(parent)

        self.container = QVBoxLayout()


class GlyphyApp(QMainWindow):
    '''Top-level Application for GlyphyType app'''
    def __init__(self, parent=None):
        super(GlyphyApp, self).__init__(parent)

        # Application metadata
        self.appTitle = 'GlyphyType'

        # Build the UI
        self.setWindowTitle(self.appTitle)
        self.setGeometry(100, 100, 1200, 900)
        self.buildWidgets()

    def buildWidgets(self):
        '''Constructs the user interface for the app'''
        # Build the Main toolbar
        self.buildMainToolbar()

        # Build the main container  
        self.container = Container()

        # Build the Utility Toolbar
        self.buildUtilityToolbar()

        # Build the canvas
        self.buildCanvas()

        # Build the Navigation Toolbar
        self.buildNavigationToolbar()

        # Set the layout
        self.container.setLayout(self.container.container)
        self.setCentralWidget(self.container)

    def buildMainToolbar(self):
        '''Constructs the main app toolbar (File, Edit, Help, etc.)'''
        # Create menubar widget
        self.mainMenuBar = self.menuBar()

        # Create File menu
        self.fileMenu = QMenu('&File')
        self.fileMenu.addAction('&New Font', self.newFont, 'Ctrl+N')
        self.fileMenu.addAction('&New Glyph', self.newGlyph, 'Ctrl+Shift+N')
        self.fileMenu.addSeparator()
        self.fileMenu.addAction('&Import Font', self.importFont, 'Ctrl+O')
        self.fileMenu.addAction('&Export Font', self.exportFont, 'Ctrl+S')
        self.fileMenu.addSeparator()
        self.fileMenu.addAction('E&xit', self.quit, 'Ctrl+Q')
        self.mainMenuBar.addMenu(self.fileMenu)

        # Create Edit menu
        self.editMenu = QMenu('&Edit')
        self.editMenu.addAction('&Undo', self.undo, 'Ctrl+Z')
        self.editMenu.addAction('&Redo', self.redo, 'Ctrl+Y')
        self.editMenu.addSeparator()
        self.editMenu.addAction('&Cut', self.cut, 'Ctrl+X')
        self.editMenu.addAction('C&opy', self.copy, 'Ctrl+C')
        self.editMenu.addAction('&Paste', self.paste, 'Ctrl+V')
        self.editMenu.addSeparator()
        self.editMenu.addAction('Clear &All', self.clearCanvas, 'Ctrl+W')
        self.mainMenuBar.addMenu(self.editMenu)

        # Create Tools menu
        self.toolsMenu = QMenu('&Tools')
        self.toolsMenu.addAction('&Brush', self.selectBrushTool, 'Ctrl+B')
        self.toolsMenu.addAction('&Line', self.selectLineTool, 'Ctrl+L')
        self.toolsMenu.addSeparator()
        self.toolsMenu.addAction('&Ellipse', self.selectEllipseTool, 'Ctrl+E')
        self.toolsMenu.addAction('&Rectangle', self.selectRectangleTool, 'Ctrl+R')
        self.toolsMenu.addAction('Trian&gle', self.selectTriangleTool, 'Ctrl+T')
        self.toolsMenu.addSeparator()
        self.toolsMenu.addAction('Er&aser', self.selectEraserTool, 'Esc')
        self.toolsMenu.addAction('&Fill Color', self.selectFillTool, 'Ctrl+F')
        self.toolsMenu.addSeparator()
        self.toolsMenu.addAction('Show/&Hide Reference', self.toggleReference, 'Ctrl+/')
        self.mainMenuBar.addMenu(self.toolsMenu)

        # Create the Help menu
        self.helpMenu = QMenu('&Help')
        self.helpMenu.addAction('&Tutorial', self.showTutorial)
        self.helpMenu.addAction('&Documentation', self.showDocumentation)
        self.mainMenuBar.addMenu(self.helpMenu)

        # Create the About menu
        self.aboutMenu = QMenu('&About')
        self.aboutMenu.addAction('&About GlyphyType', self.showAbout)
        self.aboutMenu.addAction('&Source', self.showSource)
        self.mainMenuBar.addMenu(self.aboutMenu)

    def buildUtilityToolbar(self):
        '''Constructs the Utility Toolbar with drawing tools, etc.'''
        self.utilityToolbar = UtilityToolbar()
        self.container.container.addWidget(self.utilityToolbar)

    def buildCanvas(self):
        '''Constructs the drawing canvas for the user to draw glyphs on.'''
        self.canvas = Canvas(self)
        self.canvas.setFixedSize(1180, 700)
        self.container.container.addWidget(self.canvas)

    def buildNavigationToolbar(self):
        '''Constructs the Navigation Toolbar for the user
        to move to next/previous glyphs, and show/hide reference.'''
        self.navigationToolbar = NavigationToolbar()
        self.container.container.addWidget(self.navigationToolbar)

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
        '''Exits the application.'''
        pass

    def undo(self):
        '''Undoes the last stored action from the program history.'''
        pass

    def redo(self):
        '''Redoes the last stored action from the program history.'''
        pass

    def cut(self):
        '''Cuts the selection to the clipboard.'''
        pass

    def copy(self):
        '''Copies the selection to the clipboard.'''
        pass

    def paste(self):
        '''Pastes the clipboard contents to the canvas.'''
        pass

    def clearCanvas(self):
        '''Completely clears the canvas.'''
        pass

    def selectBrushTool(self):
        '''Sets the current tool to brush tool'''
        pass

    def selectLineTool(self):
        '''Sets the current tool to line tool.'''
        pass

    def selectEllipseTool(self):
        '''Sets the current tool to the ellipse tool.'''
        pass

    def selectRectangleTool(self):
        '''Sets the current tool to the rectangle tool.'''
        pass

    def selectTriangleTool(self):
        '''Sets the current tool to the triangle tool.'''
        pass

    def selectEraserTool(self):
        '''Sets the current tool to the eraser tool.'''
        pass

    def selectFillTool(self):
        '''Sets the current tool to the color fill tool.'''
        pass

    def toggleReference(self):
        '''Toggles the reference watermark on the canvas for the current glyph.'''
        pass

    def showTutorial(self):
        '''Brings up tutorial docs in browser.'''
        pass

    def showDocumentation(self):
        '''Brings up the documentation docs in browswer.'''
        pass

    def showAbout(self):
        '''Brings up small window with "About" info.'''
        pass

    def showSource(self):
        '''Brings up the GitHub repo in browser.'''
        pass




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GlyphyApp()
    window.show()
    sys.exit(app.exec_())