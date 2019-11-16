# -*- coding: utf-8 -*-
"""
Class Tree and usufull functions for Prefix Trees homework
"""

# General Tree class
# ------------------------------------------------------------------------------

class Tree:
    """
    Simple class for General Tree
    """

    def __init__(self, key=None, children=None):
        """
        Init General Tree, children is [] if not given
        """
        self.key = key
        if children is not None:
            self.children = children
        else:
            self.children = []

    @property
    def nbchildren(self):
        return len(self.children)

    

# measures
#------------------------------------------------------------------------------

def size(T):
    s = 1
    for i in range(T.nbchildren):
        s += size(T.children[i])
    return s


# height

def height(T):
    h = -1
    for child in T.children:
        h = max(h, height(child))
    return h + 1
    
# External Path Length
        
def epl(T, h=0):
    """
    External Path Length
    """
    if T.nbchildren > 0:
        length = 0
        for i in range(T.nbchildren):
            length += epl(T.children[i], h+1)
        return length
    else:
        return h
