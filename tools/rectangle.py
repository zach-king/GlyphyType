'''
File:       rectanlge.py
Description: 
            Implements the Rectangle tool used by the 
            Canvas class. This tool implements the 
            required methods by the interface Tool.

            The Rectangle tool is a basic drawing 
            tool; you click once to start the top 
            left corner of the rectanlge graphic
            and then drag down and to the right
            to move the bottom right corner, 
            and finally release the mouse button 
            to create the rectanlge.
'''

from . import tool
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Rectangle(tool.Tool):
    def __init__(self, canv):
        super(Rectangle, self).__init__(canv)
        self.origin = QPoint() # the origin of the rectangle (top-left corner)
        self.startPoint = None
        self.stopPoint = None
        self.width = 0
        self.height = 0

    def mousePress(self, event):
        if event.button() == Qt.LeftButton:
            self.startPoint = event.pos()
            self.stopPoint = event.pos()
            self.canvas.isDrawing = True

    def mouseRelease(self, event):
        if event.button() == Qt.LeftButton and self.canvas.isDrawing:
            self.canvas.isDrawing = False
            self.calculateCorners()
            self.canvas.drawRectangle(self.origin, self.width, self.height)
            self.startPoint = None
            self.stopPoint = None
            self.width = 0
            self.height = 0

    def mouseMove(self, event):
        if (event.buttons() & Qt.LeftButton) and self.canvas.isDrawing:
            self.stopPoint = event.pos()

    def calculateCorners(self):
        self.width = abs(self.stopPoint.x() - self.startPoint.x())
        self.height = abs(self.stopPoint.y() - self.startPoint.y())
        
        self.origin.setX(min(self.startPoint.x(), self.stopPoint.x()))
        self.origin.setY(min(self.startPoint.y(), self.stopPoint.y()))

        