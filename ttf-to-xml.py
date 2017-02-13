#A quick example of how to convert a truetype font file to a modifiable xml document.
from fontTools.ttLib import TTFont

font = TTFont('cour.ttf')
font.saveXML('cour.xml')

xml = xml('cour - Copy.xml')
xml.saveTTFont('cour - Copy.ttf')
