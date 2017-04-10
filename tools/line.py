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
        self.origin = None
        self.startPoint = None
        self.stopPoint = None

    def mousePress(self, event):
        super(Line, self).mouseMove(event)
        if event.button() == Qt.LeftButton:
            # Add the point to vertices
            self.vertices.append((event.pos().x(), event.pos().y()))

            # Check if started yet
            if self.startPoint == None:
                # Start new line segment
                if self.origin == None:
                    self.origin = event.pos()

                self.startPoint = event.pos()
                self.canvas.lastPoint = event.pos()
                self.canvas.isDrawing = True
            else:
                # Stop drawing, because already have a start point
                self.stopPoint = event.pos()
                self.canvas.isDrawing = False
                self.canvas.drawLineTo(event.pos())

        elif event.button() == Qt.RightButton and self.origin != None:
            self.canvas.drawLineTo(self.origin)
            self.canvas.isDrawing = False
            self.canvas.lastPoint = None
            self.startPoint = None
            self.origin = None
            self.canvas.addPath(self.vertices)