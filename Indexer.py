# Indexer.py
# Rutu Patel
# rpatel53@stu.parkland.edu
# CSC 220, Spring 2017

from avl_tree import AVLTreeMap
import time
from unsorted_table_map import UnsortedTableMap
from sorted_table_map import SortedTableMap
from chain_hash_map import ChainHashMap
from probe_hash_map import ProbeHashMap
from splay_tree import SplayTreeMap
from red_black_tree import RedBlackTreeMap
from collections import OrderedDict

class Indexer:
    def __init__(self, original, preprocessed, typeOfMap ,index=None ):
        self.__original = original
        self.__preprocessed = preprocessed
        self.__typeOfMap = typeOfMap
        if self.__typeOfMap:
            if self.__typeOfMap == 'avl':
                self.__map = AVLTreeMap()
            elif self.__typeOfMap == 'unsorted':
                self.__map = UnsortedTableMap()
            elif self.__typeOfMap == 'sorted':
                self.__map = SortedTableMap()
            elif self.__typeOfMap == 'chain':
                self.__map = ChainHashMap()
            elif self.__typeOfMap == 'probe':
                self.__map = ProbeHashMap()
            elif self.__typeOfMap == 'splay':
                self.__map = SplayTreeMap()
            elif self.__typeOfMap == 'rb':
                self.__map = RedBlackTreeMap()
            elif self.__typeOfMap == 'dict':
                self.__map = dict()
            elif self.__typeOfMap == 'od':
                self.__map = OrderedDict()
        self.__indexFile = index
        self.__stats = [0, 0, 0]

    def index(self):
        filename = self.__preprocessed
        startIndex = time.time()
        freq = {}
        line_number = 0
        totalWords = 0
        for piece in open(filename).readlines():
            line_number += 1
            # RP: Piece has lines, and word is splitting lines
            for word in piece.split():
                if word in self.__map:
                    self.__map[word].append(line_number)
                else:
                    self.__map[word] = [line_number]
                freq[word] = 1 + freq.get(word, 0)
                totalWords += 1
        endIndex = time.time()
        timeIndex = endIndex - startIndex
        uniqueWords = len(freq)
        average = totalWords / uniqueWords
        frequencies = sorted(value for value in freq.values())
        if len(frequencies) % 2 == 1:
            median = frequencies[len(frequencies) // 2]
        else:
            median = frequencies[((len(frequencies) // 2) +
                                  len(frequencies) // 2 - 1) // 2]

        self.__stats = [timeIndex, average, median]

    def UserInterface(self):
        print("Map used:", self.__typeOfMap)
        print(self)
        with open(self.__original, 'r') as infile:
            originalText = infile.readlines()
            while True:
                self.__search(originalText)
                answer = input("Quit?")
                if answer.startswith('y'):
                    if self.__indexFile is not None:
                        self.__writeIndexFile()
                    break

    def __repr__(self):
        output = "---------------------------------------\n"
        output += "Stats for {} :\n\n".format(self.__original)
        output += "Index took {:.2f} seconds to create.\n".format(
            self.__stats[0])
        output += "Total number of indexed terms: {:>8}\n".format(
            len(self.__map))
        output += "Average word frequency: {:15.2f}\n".format(self.__stats[1])
        output += "Median word frequency: {:>16}\n".format(self.__stats[2])
        output += "---------------------------------------\n"
        return output

    def __search(self, originalText):
        searchWord = input("Enter a word to seach for : ")
        foundLineNumbers = []
        startSearch = time.time()
        if searchWord in self.__map.keys():
            foundLineNumbers = self.__map[searchWord]  # List of lines
        else:
            print(searchWord, "doesn't exist.")
        endSearch = time.time()
        searchTime = endSearch - startSearch
        for lineNumber in foundLineNumbers:
            print(lineNumber, ':', originalText[lineNumber - 1])
        print(searchWord, "occured", len(foundLineNumbers), "times.")
        print("And searching took only ", searchTime, "seconds.")

    def __writeIndexFile(self):
        with open(self.__indexFile, 'w') as outfile:
            for words in self.__map:
                lineNumbers = str(self.__map[words])
                outfile.write(words + ' ' + lineNumbers[1:-2] + "\n")
