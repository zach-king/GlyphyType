'''
File:       canvas.py
Description: 
            Implements the custom GlyphyType canvas widget
            for drawing characters/glyphs. 
'''

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Canvas(QWidget):
    def __init__(self, parent=None):
        super(Canvas, self).__init__(parent)

        # Set attributes by default
        self.penWidth = 1
        self.penColor = Qt.black
        self.lastPoint = QPoint()
        self.drawing = False

    def setPenWidth(self, w):
        if w <= 0:
            return
        self.penWidth = w

    def setPenColor(self, c):
        self.penColor = c

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.lastPoint = event.pos()
            self.drawing = True

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton):
            self.drawLineTo(event.pos())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton and self.drawing:
            self.drawLineTo(event.pos())
            self.drawing = False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawRect(event.rect())

    def drawLineTo(self, endPoint):
        painter = QPainter(self)
        painter.setPen(QPen(self.penColor, self.penWidth, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        painter.drawLine(self.lastPoint, endPoint)
    
        self.lastPoint = QPoint(endPoint)