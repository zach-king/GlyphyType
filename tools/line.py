'''
File:       line.py
Description: 
            Implements the Line tool used by the 
            Canvas class. This tool implements the 
            required methods by the interface Tool.

            The Line tool is a simple tool with two 
            points (start and stop). Click to create
            the first point, and then click again to 
            create the second point.
'''

from . import tool
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Line(tool.Tool):
    def __init__(self, canv):
        super(Line, self).__init__(canv)
        self.startPoint = None
        self.stopPoint = None

    def mousePress(self, event):
        if event.button() == Qt.LeftButton:
            # Check if started yet
            if self.startPoint == None:
                # Start new line segment
                self.startPoint = event.pos()
                self.canvas.lastPoint = event.pos()
                self.canvas.isDrawing = True
            else:
                # Stop drawing, because already have a start point
                self.stopPoint = event.pos()
                self.canvas.isDrawing = False
                self.canvas.drawLineTo(event.pos())

                # These lines make it so the line doesn't 
                # stay connected all the time (you make a new 
                # start and stop point each time)
                self.canvas.lastPoint = None
                self.startPoint = None

    # def mouseRelease(self, event):
    #     if event.button() == Qt.LeftButton and self.canvas.isDrawing:
    #         self.canvas.drawLineTo(event.pos())
    #         self.canvas.isDrawing = False

    # def mouseMove(self, event):
    #     if (event.buttons() & Qt.LeftButton) and self.canvas.isDrawing:
    #         self.canvas.drawLineTo(event.pos())