'''
File:       canvas.py
Description: 
            Implements the custom GlyphyType canvas widget
            for drawing characters/glyphs. 
'''

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from tools import brush, line

class Canvas(QWidget):
    def __init__(self, parent=None):
        super(Canvas, self).__init__(parent)

        self.setAttribute(Qt.WA_StaticContents)
        self.modified = False
        self.isDrawing = False
        self.penWidth = 3
        self.penColor = Qt.black
        self.currentTool = brush.Brush(self)
        imageSize = QSize(500, 500)
        self.image = QImage(imageSize, QImage.Format_RGB32)
        self.lastPoint = QPoint()
        self.paths = []
        self.parent = parent

        self.painter = QPainter()

    def openImage(self, fileName):
        loadedImage = QImage()
        if not loadedImage.load(fileName):
            return False

        w = loadedImage.width()
        h = loadedImage.height()    
        self.mainWindow.resize(w, h)

        self.image = loadedImage
        self.modified = False
        self.update()
        return True

    def saveImage(self, fileName, fileFormat):
        visibleImage = self.image
        self.resizeImage(visibleImage, self.size())

        if visibleImage.save(fileName, fileFormat):
            self.modified = False
            return True
        else:
            return False

    def setPenColor(self, newColor):
        self.penColor = newColor

    def setPenWidth(self, newWidth):
        self.penWidth = newWidth

    def clearImage(self):
        self.image.fill(qRgb(255, 255, 255))
        self.modified = True
        self.update()

    def clearCanvas(self):
        self.clearImage()
        self.paths = []

    def mousePressEvent(self, event):
        self.currentTool.mousePress(event)

    def mouseMoveEvent(self, event):
        self.currentTool.mouseMove(event)

    def mouseReleaseEvent(self, event):
        self.currentTool.mouseRelease(event)

    def paintEvent(self, event):
        self.painter.begin(self)
        self.painter.drawImage(event.rect(), self.image)
        self.painter.end()

    def resizeEvent(self, event):
        self.resizeImage(self.image, event.size())
        super(Canvas, self).resizeEvent(event)

    def drawLineTo(self, endPoint):
        self.painter.begin(self.image)
        self.painter.setPen(QPen(self.penColor, self.penWidth,
            Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        self.painter.drawLine(self.lastPoint, endPoint)
        self.modified = True

        self.update()
        self.lastPoint = QPoint(endPoint)
        self.painter.end()

    def drawLine(self, startPoint, endPoint):
        self.painter.begin(self.image)
        self.painter.setPen(QPen(self.penColor, self.penWidth,
            Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        print('Drawing segment from ({}, {}) to ({}, {})'.format(startPoint.x, startPoint.y, endPoint.x, endPoint.y))
        self.painter.drawLine(startPoint, endPoint)
        self.modified = True
        self.update()
        self.painter.end()

    def drawRectangle(self, origin, width, height):
        self.painter.begin(self.image)
        self.painter.setPen(QPen(self.penColor, self.penWidth,
            Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        self.painter.drawRect(QRect(origin, QSize(width, height)))
        self.modified = True

        self.update()
        self.painter.end()

    def drawTriangle(self, origin, base_width, height):
        self.painter.begin(self.image)
        self.painter.setPen(QPen(self.penColor, self.penWidth,
            Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        self.modified = True

    def addPath(self, list_of_vertices):
        self.paths.append(list_of_vertices)

    def resizeImage(self, image, newSize):
        if image.size() == newSize:
            return

        # this resizes the canvas without resampling the image
        newImage = QImage(newSize, QImage.Format_RGB32)
        newImage.fill(qRgb(255, 255, 255))
        painter = QPainter(newImage)
        painter.drawImage(QPoint(0, 0), image)

        self.image = newImage

    def print_(self):
        printer = QPrinter(QPrinter.HighResolution)

        printDialog = QPrintDialog(printer, self)
        if printDialog.exec_() == QDialog.Accepted:
            painter = QPainter(printer)
            rect = painter.viewport()
            size = self.image.size()
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.image.rect())
            painter.drawImage(0, 0, self.image)
            painter.end()

    def isModified(self):
        return self.modified

    def penColor(self):
        return self.penColor

    def penWidth(self):
        return self.penWidth

    def DrawPaths(self):
        '''Draws the paths stored in self. Only lines currently.'''
        # self.drawLine(QPoint(393, 23), QPoint(691, 23))
        # self.drawLine(QPoint(691, 23), QPoint(691, 419))
        # self.drawLine(QPoint(691, 419), QPoint(393, 419))
        # self.drawLine(QPoint(393, 419), QPoint(393, 23))
        # self.painter.end()
        # return
        for path in self.paths:
            startPoint = self.ParsePoint(path[0])
            origin = startPoint
            endPoint = None
            for point in path[1:]:
                endPoint = self.ParsePoint(point)
                self.drawLine(startPoint, endPoint)
                startPoint = endPoint
            endPoint = origin
            self.drawLine(startPoint, endPoint)

    def ParsePoint(self, tup):
        point = QPoint()
        point.x = tup[0]
        point.y = tup[1]
        # print('Parsed QPoint ({}, {})'.format(point.x, point.y))
        return point