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
import sys, webbrowser
import pickle

from glyphStruct import Glyph as gData
from fontTools.ttLib import TTFont

from utility_toolbar import UtilityToolbar
from navigation_toolbar import NavigationToolbar
from canvas import Canvas
from tools import line, brush, rectangle


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

        # Glyph data
        self.glyphList = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~' # don't change this 
        self.glyphPaths = dict()
        self.initializeGlyphPaths()
        self.currentGlyph = self.glyphList[0]
        self.currentGlyphIndex = 0
        self.currentFontFile = None
        self.MAX_GLYPH_INDEX = len(self.glyphList) - 1
        self.hasSaved = False

        # Build the UI
        self.setWindowTitle(self.appTitle)
        self.setGeometry(100, 100, 1120, 800)
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

        # Set initial glyph
        self.currentGlyph = self.glyphList[self.currentGlyphIndex]
        self.navigationToolbar.setCurrentGlyphDisplay(self.currentGlyph)

    def buildMainToolbar(self):
        '''Constructs the main app toolbar (File, Edit, Help, etc.)'''
        # Create menubar widget
        self.mainMenuBar = self.menuBar()

        # Create File menu
        self.fileMenu = QMenu('&File')
        self.fileMenu.addAction('&New Font', self.newFont, 'Ctrl+N')
        self.fileMenu.addAction('&Save', self.saveFont, 'Ctrl+S')
        self.fileMenu.addAction('Save &As', self.saveFontAs, 'Ctrl+Shift+S')
        self.fileMenu.addSeparator()
        self.fileMenu.addAction('&Import Font', self.importFont, 'Ctrl+O')
        self.fileMenu.addAction('&Export Font', self.exportFont, 'Ctrl+Alt+S')
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
        self.utilityToolbar = UtilityToolbar(self) # must pass self to bind buttons to selectTool methods   
        self.container.container.addWidget(self.utilityToolbar)

    def buildCanvas(self):
        '''Constructs the drawing canvas for the user to draw glyphs on.'''
        self.canvas = Canvas(self)
        self.canvas.clearImage()
        self.canvas.setFixedSize(1100, 600)
        self.container.container.addWidget(self.canvas)

    def buildNavigationToolbar(self):
        '''Constructs the Navigation Toolbar for the user
        to move to next/previous glyphs, and show/hide reference.'''
        self.navigationToolbar = NavigationToolbar(self)
        self.container.container.addWidget(self.navigationToolbar)

    def newFont(self):
        '''Menu command for constructing a new font.'''
        # Get the filename for the user's new font
        newfile = QFileDialog.getSaveFileName(self, 'New Font', filter='*.gtfo')
        if not newfile:
            return # User cancelled

        # Set the current file path to newfile 
        self.currentFontFile = newfile 
        self.glyphPaths = dict()
        self.initializeGlyphPaths()
        self.currentGlyphIndex = 0
        self.currentGlyph = self.glyphList[self.currentGlyphIndex]

    def saveFont(self):
        '''Saves font data to currentFontFile.'''
        # Check for existing font file name
        if not self.currentFontFile:
            self.currentFontFile = QFileDialog.getSaveFileName(self, 'Save Font', filter='*.gtfo')
            if not self.currentFontFile:
                return

        # Write dictionary of paths to file
        self.serializeFont()

        # Set saved flag
        self.hasSaved = True

    def saveFontAs(self):
        '''Save As dialog for saving currentFontFile.'''
        # Get new filename
        self.currentFontFile = QFileDialog.getSaveFileName(self, 'Save Font', filter='*.gtfo')
        if not self.currentFontFile:
            return

        # Write dictionary of paths to file
        self.serializeFont()

        # Set saved flag
        self.hasSaved = True

    def importFont(self):
        '''Menu command for importing a GlyphyType font.'''
        # Get the existing font file 
        fontfile = QFileDialog.getOpenFileName(self, 'Import Font', filter='*.gtfo')
        if not fontfile:
            return 

        # Check if need to save existing 
        if self.currentFontFile != None:
            self.checkSave()

        # Set current font to opened one
        self.currentFontFile = fontfile

        # Reset and go back to first glyph
        self.currentGlyphIndex = 0
        self.currentGlyph = self.glyphList[self.currentGlyphIndex]

        # Deserialize (parse) font file that was opened
        self.deserializeFont()

        print(self.glyphPaths[0])


        # Show current font now from new font file that was opened
        self.showCurrentGlyph()


    def showCurrentGlyph(self):
        '''Alternative method for showing the current glyph based off the currentFontFile and indices'''
        # Clear canvas
        self.clearCanvas()

        # Restore any existing canvas paths
        self.canvas.paths = self.glyphPaths[self.currentGlyphIndex]
        
        # Show current glyph
        self.navigationToolbar.setCurrentGlyphDisplay(self.currentGlyph)

        if self.canvas.paths != []:
            self.canvas.DrawPaths()

        print('Current glyph: ' + self.glyphList[self.currentGlyphIndex] + '\n')
        print(self.glyphPaths[self.currentGlyphIndex])
        print('\n\n')

    def checkSave(self):
        '''Check if user has saved work or not (used before closing, etc.)'''
        if not self.hasSaved:
            # Ask user if they want to save
            proceed = QMessageBox.question(self, 'Warning', 
                'You have unsaved progress. Are you sure you want to continue?', 
                QMessageBox.No, QMessageBox.Yes)

            if proceed == QMessageBox.No:
                # Save
                self.saveFont()

    def exportFont(self):
        '''Menu command for exporting a GlyphyType font.'''
        self.checkSave()

        glyphList = []
        for idNum in self.glyphPaths:
            g = gData(self.glyphPaths[idNum], idNum)
            g.align()
            g.scale()
            glyphList.append(g)
            # print(g.name)


        fontName = self.currentFontFile
        if self.currentFontFile.endswith('.gtfo'):
            fontName = fontName.split('.gtfo')[0]
            
        with open('emptyGlyphs.xml') as foundation, open(fontName + '.ttx', 'w+') as newTable:
            for line in foundation:
                newTable.write(line)
                for glyph in glyphList:
                    if ("<TTGlyph name=\"" + str(glyph.name) + "\"") in line:
                        # print("Writing " + str(glyph.name) + "(" + str(glyph.id) + "): ")
                        newTable.write(glyph.writeFormat())

        tt = TTFont()
        tt.importXML(fontName + '.ttx')
        tt.save(fontName + '.ttf')


    def quit(self):
        '''Exits the application.'''
        self.checkSave()
        exit()

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
        self.canvas.clearCanvas()

    def selectBrushTool(self):
        '''Sets the current tool to brush tool'''
        self.canvas.currentTool = brush.Brush(self.canvas)

    def selectLineTool(self):
        '''Sets the current tool to line tool.'''
        self.canvas.currentTool = line.Line(self.canvas)

    def selectEllipseTool(self):
        '''Sets the current tool to the ellipse tool.'''
        pass

    def selectRectangleTool(self):
        '''Sets the current tool to the rectangle tool.'''
        self.canvas.currentTool = rectangle.Rectangle(self.canvas)

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
        aboutBox = QMessageBox(self)
        aboutBox.setIcon(QMessageBox.Information)

        # Read in the about text from file
        text = ''
        with open('./about.md', 'r') as fin:
            text = fin.read()

        aboutBox.setText('About')
        aboutBox.setInformativeText(text)
        aboutBox.setWindowTitle('About GlyphyType')
        aboutBox.show()

    def showSource(self):
        '''Brings up the GitHub repo in browser.'''
        webbrowser.open('https://github.com/zach-king/GlyphyType')

    def prevGlyph(self):
        '''Go to the previous glyph in the series.'''
        # Switch to previous glyph and display it (tries to at least)
        if (self.currentGlyphIndex > 0):
            # Serialize the current glyph points
            paths = self.canvas.paths
            self.glyphPaths[self.currentGlyphIndex] = paths

            # Clear the canvas
            self.clearCanvas()

            self.currentGlyph = self.glyphList[self.currentGlyphIndex - 1]
            self.currentGlyphIndex -= 1

            self.showCurrentGlyph()

    def nextGlyph(self):
        '''Go to the next glyph in the series.'''
        # Switch to previous glyph and display it (tries to at least)
        if (self.currentGlyphIndex < self.MAX_GLYPH_INDEX):
            # Serialize the current glyph points
            paths = self.canvas.paths
            self.glyphPaths[self.currentGlyphIndex] = paths

            # Clear the canvas
            self.clearCanvas()

            self.currentGlyph = self.glyphList[self.currentGlyphIndex + 1]
            self.currentGlyphIndex += 1

            self.showCurrentGlyph()

    def serializeFont(self):
        '''Serializes current font's paths to file.'''
        with open(self.currentFontFile, 'wb') as fout:
            pickle.dump(self.glyphPaths, fout)

    def deserializeFont(self):
        '''Parses current font's paths from file.'''
        self.glyphPaths = dict()
        self.initializeGlyphPaths()
        self.currentGlyphIndex = 0
        with open(self.currentFontFile, 'rb') as fin:
            self.glyphPaths = pickle.load(fin)

    def initializeGlyphPaths(self):
        self.glyphPaths = dict()
        for index in range(len(self.glyphList)):
            self.glyphPaths[index] = list()
                



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GlyphyApp()
    window.show()
    sys.exit(app.exec_())