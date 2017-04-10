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

class Triangle(tool.Tool):
    def __init__(self, canv):
        super(Triangle, self).__init__(canv)
        self.origin = QPoint() # the origin of the triangle (bottom  corner)
        self.startPoint = None
        self.stopPoint = None
        self.base_width = 0
        self.height = 0

    def mousePress(self, event):
        super(Triangle, self).mouseMove(event)
        if event.button() == Qt.LeftButton:
            self.startPoint = event.pos()
            self.stopPoint = event.pos()
            self.canvas.isDrawing = True

    def mouseRelease(self, event):
        super(Triangle, self).mouseMove(event)
        if event.button() == Qt.LeftButton and self.canvas.isDrawing:
            self.canvas.isDrawing = False
            self.calculateVertices()
            self.canvas.drawRectangle(self.origin, self.width, self.height)
            self.startPoint = None
            self.stopPoint = None
            self.width = 0
            self.height = 0

    def mouseMove(self, event):
        super(Triangle, self).mouseMove(event)
        if (event.buttons() & Qt.LeftButton) and self.canvas.isDrawing:
            self.stopPoint = event.pos()

    def calculateVertices(self):
        self.width = abs(self.stopPoint.x() - self.startPoint.x())
        self.height = abs(self.stopPoint.y() - self.startPoint.y())
        
        self.origin.setX(min(self.startPoint.x(), self.stopPoint.x()))
        self.origin.setY(min(self.startPoint.y(), self.stopPoint.y()))

        