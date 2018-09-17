# project4.py
# Rutu Patel
# rpatel53@stu.parkland.edu
# CSC 220, Spring 2017

import argparse
import sys
from Indexer import Indexer

if __name__ == '__main__':
    # First create the parser object.
    # description will be printed when some calls the program
    # with the -h or --help args.
    parser = argparse.ArgumentParser(description='Project 4 Driver file.')

    # Add a required original file name.
    parser.add_argument('original', help='The Original text file name.')

    # Add a required preprocesed file name.
    parser.add_argument('preprocessed',
                        help='The Preprocessed file for building the index.')

    # Add an optional map used argument. The 'dest' arg is how
    # it will be referred to inside the parser.
    parser.add_argument('--map',
                help='The requested multimap data structure.', default='avl')

    # Add an optional Index file name. The 'dest' arg is how
    # it will be referred to inside the parser.
    parser.add_argument('--index',
                        dest='index', help='The optional Index file name.')

    # If no input use supplied, that will be handled by argparse,
    # since it was a required argument.
    # Get the args for use.
    args = parser.parse_args()
    if args.index:
        myIndexer = Indexer(args.original,args.preprocessed,
                            args.map,args.index)
    else:
        myIndexer = Indexer(args.original,args.preprocessed,args.map)

    myIndexer.index()
    myIndexer.UserInterface()
