#Move to class variable of Glyph object
idDict = {0:'exclam', 1:'quotedbl', 2:'numbersign', 3:'dollar',
          4:'percent', 5:'ampersand', 6:'quotesingle', 7:'parenleft',
          8:'parenright', 9:'asterisk', 10:'plus', 11:'comma',
          12:'hyphen', 13:'period', 14:'slash', 15:'zero',
          16:'one', 17:'two', 18:'three', 19:'four',
          20:'five', 21:'six', 22:'seven', 23:'eight',
          24:'nine', 25:'colon', 26:'semicolon', 27:'less',
          28:'equal', 29:'greater', 30:'question', 31:'at',
          32:'A', 33:'B', 34:'C', 35:'D',
          36:'E', 37:'F', 38:'G', 39:'H',
          40:'I',41:'J', 42:'K', 43:'L',
          44:'M', 45:'N', 46:'O', 47:'P',
          48:'Q', 49:'R', 50:'S', 51:'T',
          52:'U', 53:'V', 54:'W', 55:'X',
          56:'Y', 57:'Z', 58:'bracketleft', 59:'backslash',
          60:'bracketright', 61:'asciicircum', 62:'underscore', 63:'grave',
          64:'a', 65:'b', 66:'c', 67:'d',
          68:'e', 69:'f', 70:'g', 71:'h',
          72:'i', 73:'j', 74:'k', 75:'l',
          76:'m', 77:'n', 78:'o', 79:'p',
          80:'q', 81:'r', 82:'s', 83:'t',
          84:'u', 85:'v', 86:'w', 87:'x',
          88:'y', 89:'z', 90:'braceleft', 91:'bar',
          92:'braceright', 93:'asciitilde'
          }

metricsDict = {0:[38,int(-3),145,797], 1:[28,542,246,797],
               2:[22,0,496,783], 3:[41,int(-20),351,803],
               4:[46,int(-8),565,790], 5:[33,-10,418,823],
               6:[28,542,110,797], 7:[87,int(-210),273,959],
               8:[14,int(-210),200,959], 9:[32,382,409,783],
               10:[46,160,485,599], 11:[19,int(-149),132,107],
               12:[27,343,278,416], 13:[28,-3,132,107],
               14:[6,int(-120), 347, 869], 15:[41,-14,363,797],
               16:[15,0,191,783], 17:[29,0,340,797],
               18:[33,-14,352,797], 19:[22,0,368,783],
               20:[30,int(-14),341,783], 21:[41,int(-14),352,797],
               22:[22,0,305,783], 23:[28,int(-14),355,797],
               24:[41,int(-14),352,797], 25:[51,47,155,441],
               26:[42,int(-99),155,441], 27:[46,182,485,576],
               28:[46,243,485,515], 29:[46,182,485,576],
               30:[26,int(-3),331,803], 31:[31,int(-189),654,707],
               32:[18,0,377,783], 33:[46,0,369,783],
               34:[41,int(-14),352,797], 35:[46,0,364,783],
               36:[46,0,305,783], 37:[46,0,316,783],
               38:[41,int(-14),352,797], 39:[46,0,369,783],
               40:[46,0,138,783], 41:[20,int(-14),331,783],
               42:[46,0,374,783], 43:[46,0,285,783],
               44:[46,0,489,783], 45:[46,0,359,783],
               46:[41,int(-14),363,797], 47:[46,0,364,783],
               48:[41,int(-89),398,797], 49:[46,0,366,783],
               50:[25,int(-14),347,797], 51:[20,0,288,783],
               52:[44,int(-14),366,783], 53:[18,0,377,783],
               54:[22,0,555,783], 55:[13,0,395,783],
               56:[13,0,399,783], 57:[28,0,332,783],
               58:[87,int(-210),273,959], 59:[6,-120,347,869],
               60:[14,int(-210),200,959], 61:[29,344,423,783],
               62:[0,int(-125),428,int(-66)], 63:[75,659,260,817],
               64:[27,int(-8),340,619], 65:[46,int(-8),359,815],
               66:[41,int(-8),337,619], 67:[41,int(-8),354,815],
               68:[41,int(-8),339,619], 69:[12,0,303,823],
               70:[3,int(-171),386,619], 71:[46,0,359,815],
               72:[38,0,142,806], 73:[int(-71),int(-183),158,806],
               74:[46,0,362,815], 75:[46,0,135,815],
               76:[46,0,567,619], 77:[46,0,359,619],
               78:[41,int(-8),345,619], 79:[46,int(-171),359,619],
               80:[41,int(-171),354,619], 81:[46,0,301,619],
               82:[27,int(-8),337,619], 83:[12,int(-8),298,754],
               84:[44,int(-8),353,611], 85:[19,0,360,611],
               86:[22,0,520,611], 87:[13,0,404,611],
               88:[44,int(-171),353,611], 89:[27,0,321,611],
               90:[32,int(-210),273,959], 91:[87,-160,160,909],
               92:[14,int(-210),255,959], 93:[46,291,485,466]
               }

#When you get to clockwise ordering...
class Glyph:
    #Path is the list of contour paths that define a glyph.
    def __init__(self, path, id):
        self.id = int(id)
        self.path = path
        self.nContours = len(path)
        self.name = idDict[id]
        self.metrics = metricsDict[id]

    #Find sum of all points in a contour. Used to determine counter/clockwise ordering.
    def pointSum(self, contour, index):
        point = contour[index]
        if index < len(contour)-1:
            nextPoint = contour[index+1]
            ret = (nextPoint[0]-point[0])*(nextPoint[1]+point[1])
            return ret + self.pointSum(contour, index+1)
        else:
            nextPoint = contour[0]
            ret = (nextPoint[0]-point[0])*(nextPoint[1]+point[1])
            return ret

    #Bring path into correct ordering
    #Path => Contours => points => (x,y)
    def align(self):
        #Obtain first point
        try:
            iPoint = self.path[0][0]
            for conIndex in range(len(self.path)):
                contour = self.path[conIndex]
                total = self.pointSum(contour, 0) #Recursive sum function
                if total < 0:
                    self.path[conIndex] = contour[::-1]
        except:
            None
            
    #Bring path vertices into ratio of font metrics.
    #Canvas metrics are 1100x600 pixels.
    #Consider importing glyph sizes? Perhaps write another dimension dictionary?
    def scale(self):
        xmin = self.metrics[0]
        ymin = self.metrics[1]
        xMax = self.metrics[2]
        yMax = self.metrics[3]
        largest = 0
        contour = []
        for conIndex in range(len(self.path)):
            contourXMax = 1
            contourYMax = 1
            contour = self.path[conIndex]
            for pIndex in range(len(contour)):
                if contour[pIndex][0] > contourXMax:
                    contourXMax = contour[pIndex][0]
                if contour[pIndex][1] > contourYMax:
                    contourYMax = contour[pIndex][1]
            for pIndex in range(len(contour)):
                x = int((contour[pIndex][0]/contourXMax)*(xMax - xmin))
                y = int((600 - contour[pIndex][1]))
                y = int((y/contourYMax)*(yMax-ymin))
                contour[pIndex] = (x,y)

    #Writes a string for the contour data of a glyph file.
    def writeFormat(self):
        ret = ""
        for contour in self.path:
            ret += "\t\t<contour>\n"
            for point in contour:
                ret += ("\t\t\t<pt x=\"" + str(point[0]) +"\" y=\"" + str(point[1]) + "\" on=\"1\"/>\n")
            ret += "\t\t</contour>\n"
            ret += "\t\t<instructions>\n"
            ret += "\t\t\t<assembly>\n\t\t\t</assembly>\n"
            ret += "\t\t</instructions>\n"
        return ret
