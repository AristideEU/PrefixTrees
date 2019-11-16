# -*- coding: utf-8 -*-from __future__ import unicode_literals
__license__ = 'Nathalie (c) EPITA'
__docformat__ = 'reStructuredText'
__revision__ = '$Id: prefixtrees.py 2019-10-08'

"""
Prefix Trees homework
2019-10
@author: aristide.cuny
"""

from algopy import tree

###############################################################################
# Do not change anything above this line, except your login!
# Do not add any import



##############################################################################
## Measure

def countwords(T):
    """ count words in tree T
    
    """
    #FIXME
    c = 0
    if (T.key and T.key[1]):
        c += 1
    for kid in T.children:
        c += countwords(kid)
    return c
    
def longestwordlength(T):
    """ longest word length
    
    """
    return tree.height(T)
    
def averagelength(T):
    """ average word length
    """
    (acc, amount) = length_rec(T,0)
    return acc/amount
    

def length_rec(T, depth):
    acc = 0;
    amount = 0;
    if T.key[1]:
        acc += depth
        amount += 1
    for kid in T.children:
        a = 0
        am = 0
        (a,am) = length_rec(kid,depth + 1)
        acc += a
        amount += am
    return (acc,amount)
###############################################################################
## search and list

def searchword(T, word):
    """ search for a word in a tree
    
    """
    s = False
    for kid in T.children:
        s = s or recsearch(kid, word.strip(), 0)
    return s

def recsearch(T, word, index):
    
    if(index < len(word) and T.key[0] == word[index]):
        index += 1
        if (index == len(word)):
            return T.key[1]
        for kid in T.children:
            if recsearch(kid, word, index):
                return True
    return False

def wordlist(T):
    """ generate the word list
    
    """
    return recW(T, "")
    
def recW(T, word):
    L = []
    if T:
        word += T.key[0]
        if (T.key[1]):
            L.append(word)
        for kid in T.children:
            L += recW(kid, word)
    return L
###############################################################################
## fill-in

def completion(T,prefix):
    L = []
    L += recompletion(T, "",prefix)
    return L

def recompletion(T, pre, fix):
    if not fix:
        w = wordlist(T)
        out = []
        for i in range(len(w)):
            out.append(pre[:-1] + w[i])
        return out
    for kid in T.children:
        if kid.key[0] == fix[0]:
            return recompletion(kid, pre + fix[0], fix[1:])
    return []
    
def search_hangman(T, pattern):
    """Find all solutions to a Hangman puzzle: 
        words that match the "pattern" where letters to fill are replaced by '_'
    
    """
    L = []
    for kid in T.children:
        L += _hangman(kid, pattern, 0, "")
    return L

def _hangman(T, pattern, index, word):
    L = []
    if (index < len(pattern)):
        if(T.key[0] == pattern[index] or pattern[index] == '_'):
            index += 1
            word += T.key[0]
            for kid in T.children:
                L += _hangman(kid, pattern, index, word)
            if(index == len(pattern) and T.key[1]):
                L.append(word)
    return L
###############################################################################
## Build

def treetofile(T, filename):
    """ save the tree in a file
    
    """
    #FIXME
    """reading = open(filename, "r")
    content = reading.read().splitlines()
    """
    L = wordlist(T)
    """
    for item in content:
        if searchword(T, item):
            L.remove(item)
    reading.close()"""
    writing = open(filename, "w")
    for word in L:
        writing.write(word + "\n")
    writing.close()
    return
    
def addword(T, word):
    """ add a word in the tree
    
    """
    #FIXME
    _addword(T, word, -1)
    return

def _addword(T, word, index):
    index += 1
    if index < len(word):
        notfound = True
        i = 0
        """
        if not T.children:
            bb = Tree((word[index],index = len(word)),[])
            _addword(bb, word, index)
            T.children.append(bb)
        """
        for kid in T.children:
            if(kid.key[0] == word[index]):
                _addword(kid, word, index)
                notfound = False
                break
            if(kid.key[0] > word[index]):
                bb = tree.Tree((word[index], index == len(word)), [])
                _addword(bb, word, index)
                T.children.insert(i, bb)
                notfound = False
                break
            i += 1
        if (notfound and index < len(word)):
            bb = tree.Tree((word[index], index == len(word)), [])
            _addword(bb, word, index)
            T.children.append(bb)
    if(index == len(word)):
        T.key = (T.key[0], True)
    return
        
def treefromfile(filename):
    """ build the prefix tree from a file of words
    
    """
    reading = open(filename, "r")
    T = tree.Tree(('', False), [])
    content = reading.read().splitlines()
    for item in content:
        addword(T, item)
    reading.close()
    return T