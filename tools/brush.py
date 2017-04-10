'''
File:       brush.py
Description: 
            Implements the Brush tool used by the 
            Canvas class. This tool implements the 
            required methods by the interface Tool.

            The Brush tool is the most basic drawing 
            tool; it is the 'Pencil' tool in MS Paint.
            You click and drag to draw, and release to 
            stop drawing.
'''

from . import tool
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Brush(tool.Tool):
    def __init__(self, canv):
        super(Brush, self).__init__(canv)

    def mousePress(self, event):
        super(Brush, self).mousePress(event)
        if event.button() == Qt.LeftButton:
            self.canvas.lastPoint = event.pos()
            self.canvas.isDrawing = True

    def mouseRelease(self, event):
        super(Brush, self).mouseRelease(event)
        if event.button() == Qt.LeftButton and self.canvas.isDrawing:
            self.canvas.drawLineTo(event.pos())
            self.canvas.isDrawing = False

    def mouseMove(self, event):
        super(Brush, self).mouseMove(event)
        if (event.buttons() & Qt.LeftButton) and self.canvas.isDrawing:
            self.canvas.drawLineTo(event.pos())