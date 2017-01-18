'''
This file tells Python to treat the current directory (./GlyphyType/) as 
a Python package. Hence, it allows us to `import GlyphyType` for use outside 
of this application. This might be useful for extendinng GlyphyType in the future, 
or simply for testing purposes. 

Each .py file we create in this directory is a "module" and the string name should 
be appended to the following list. 

For example, if we had a "fontmanager.py" file, 
we would have `__all__ = ['fontmanager']`
'''
__all__ = []