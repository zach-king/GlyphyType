'''
File:       tool.py
Description:
            Defines the abstract class Tool,
            which acts as an interface for 
            child classes (tools) such as the 
            Brush, Line, Rectangle, etc.
'''


class Tool(object):
    def __init__(self, canv):
        self.canvas = canv
        self.vertices = []

    def mousePress(self, event):
        self.canvas.parent.hasSaved = False
    
    def mouseRelease(self, event):
        self.canvas.parent.hasSaved = False

    def mouseMove(self, event):
        pass