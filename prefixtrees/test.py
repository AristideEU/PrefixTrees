# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Special Python function to load module with its file name
from importlib.machinery import SourceFileLoader
from algopy import tree
import prefixtreesexample
# My handout
myfile = "aristide.cuny_prefixtrees.py"
# Load module. Same result as "import mycode"
ari = SourceFileLoader('ari', myfile).load_module()

tree1 = prefixtreesexample.Tree1
tree2 = prefixtreesexample.Tree1
print(ari.countwords(tree1))
print(ari.longestwordlength(tree1))
print(ari.averagelength(tree1))
print(ari.searchword(tree1, "cas"))
print(ari.searchword(tree1, "famous"))
print(ari.wordlist(tree1))
print(ari.completion(tree1, "fan"))
print(ari.completion(tree1, "ci"))
print(ari.completion(tree1, "what"))
print(ari.search_hangman(tree1, "c_s_"))
print(ari.search_hangman(tree1, "_a__"))
print(ari.treetofile(tree1, "textFiles/wordList0.txt"))
print(ari.treetofile(tree1, "textFiles/wordList3.txt"))
ari.addword(tree2, "fal")
ari.addword(tree2, "fala")
print(ari.wordlist(tree2))
tree10 = ari.treefromfile("textFiles/wordList1.txt")
print(ari.wordlist(tree10))
tree20 = ari.treefromfile("textFiles/wordList2.txt")
print(ari.wordlist(tree20))
