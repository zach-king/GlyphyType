'''
File:       canvas.py
Description: 
            Implements the custom GlyphyType canvas widget
            for drawing characters/glyphs. 
'''

from PyQt4.QtCore import *
from PyQt4.QtGui import *


# class Canvas(QWidget):
#     def __init__(self, parent=None):
#         super(Canvas, self).__init__(parent)

#         # Set attributes by default
#         self.penWidth = 1
#         self.penColor = Qt.black
#         self.lastPoint = QPoint()
#         self.drawing = False

#     def setPenWidth(self, w):
#         if w <= 0:
#             return
#         self.penWidth = w

#     def setPenColor(self, c):
#         self.penColor = c

#     def mousePressEvent(self, event):
#         if event.button() == Qt.LeftButton:
#             self.lastPoint = event.pos()
#             self.drawing = True

#     def mouseMoveEvent(self, event):
#         if (event.buttons() & Qt.LeftButton):
#             self.drawLineTo(event.pos())

#     def mouseReleaseEvent(self, event):
#         if event.button() == Qt.LeftButton and self.drawing:
#             self.drawLineTo(event.pos())
#             self.drawing = False

#     def paintEvent(self, event):
#         painter = QPainter(self)
#         painter.drawRect(event.rect())

#     def drawLineTo(self, endPoint):
#         painter = QPainter(self)
#         painter.setPen(QPen(self.penColor, self.penWidth, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
#         painter.drawLine(self.lastPoint, endPoint)
    
#         self.lastPoint = QPoint(endPoint)

from tools import brush

class Canvas(QWidget):
    def __init__(self, parent=None):
        super(Canvas, self).__init__(parent)

        self.setAttribute(Qt.WA_StaticContents)
        self.modified = False
        self.isDrawing = False
        self.penWidth = 1
        self.penColor = Qt.black
        self.currentTool = brush.Brush(self)
        imageSize = QSize(500, 500)
        self.image = QImage(imageSize, QImage.Format_RGB32)
        self.lastPoint = QPoint()

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

    def mousePressEvent(self, event):
#       print("self.image.width() = %d" % self.image.width())
#       print("self.image.height() = %d" % self.image.height())
#       print("self.image.size() = %s" % self.image.size())
#       print("self.size() = %s" % self.size())
#       print("event.pos() = %s" % event.pos())
        self.currentTool.mousePress(event)

    def mouseMoveEvent(self, event):
        self.currentTool.mouseMove(event)

    def mouseReleaseEvent(self, event):
        self.currentTool.mouseRelease(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(event.rect(), self.image)

    def resizeEvent(self, event):
#       print "resize event"
#       print "event = %s" % event
#       print "event.oldSize() = %s" % event.oldSize()
#       print "event.size() = %s" % event.size()

        self.resizeImage(self.image, event.size())

#       if self.width() > self.image.width() or self.height() > self.image.height():
#           newWidth = max(self.width() + 128, self.image.width())
#           newHeight = max(self.height() + 128, self.image.height())
#           print "newWidth = %d, newHeight = %d" % (newWidth, newHeight)
#           self.resizeImage(self.image, QSize(newWidth, newHeight))
#           self.update()

        super(Canvas, self).resizeEvent(event)

    def drawLineTo(self, endPoint):
        painter = QPainter(self.image)
        painter.setPen(QPen(self.penColor, self.penWidth,
            Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        painter.drawLine(self.lastPoint, endPoint)
        self.modified = True

        # rad = self.penWidth / 2 + 2
        # self.update(QRect(self.lastPoint, endPoint).normalized().adjusted(-rad, -rad, +rad, +rad))
        self.update()
        self.lastPoint = QPoint(endPoint)

    def resizeImage(self, image, newSize):
        if image.size() == newSize:
            return

#       print "image.size() = %s" % repr(image.size())
#       print "newSize = %s" % newSize

# this resizes the canvas without resampling the image
        newImage = QImage(newSize, QImage.Format_RGB32)
        newImage.fill(qRgb(255, 255, 255))
        painter = QPainter(newImage)
        painter.drawImage(QPoint(0, 0), image)


##  this resampled the image but it gets messed up with so many events...       
##      painter.setRenderHint(QPainter.SmoothPixmapTransform, True)
##      painter.setRenderHint(QPainter.HighQualityAntialiasing, True)
#       
#       newImage = QImage(newSize, QImage.Format_RGB32)
#       newImage.fill(qRgb(255, 255, 255))
#       painter = QPainter(newImage)
#       srcRect = QRect(QPoint(0,0), image.size())
#       dstRect = QRect(QPoint(0,0), newSize)
##      print "srcRect = %s" % srcRect
##      print "dstRect = %s" % dstRect
#       painter.drawImage(dstRect, image, srcRect)


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