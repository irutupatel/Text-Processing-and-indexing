# preprocessor.py
# Mark Van Moer
# mvanmoer@parkland.edu
# CSC 220, Fall 2016

import sys
import argparse

def preprocess(args):
    '''Function to preprocess text. Takes an input file name, a stopword file
     name, and writes a preprocessed text file.
    * Remove (some?) punctuation and non-alphabetic characters.
    * Convert all letters to lower case.
    * Remove stopwords.
    * Remove all words with less than three characters.
    '''
    stopwordsfile = args.stopwords
    # MVM: This is rather compact, could be simply done in a loop.
    stopwords = [x.strip() for x in open(stopwordsfile, 'r').readlines()]
    
    inputtext = open(args.input, 'r')
    if args.output:
        outputtext = open(args.output, 'w')
    else:
        outputtext = sys.stdout

    stops = 0
    short = 0
    for line in inputtext:
        # Convert all to lower case.
        line = line.lower()

        # remove punctuation - strings are immutable
        stripped_line = ''
        for c in line:
            if c.isalpha() or c == "'":
                stripped_line += c
            else:
                stripped_line += ' '

        words = stripped_line.split()

        # ' needs special handling. When to remove:
        # -- when indicating possesive case: "count's"
        # -- when starting an old timey abbreviation: "'tis"
        # -- when starting an inner quotation
        # -- when contracting "had": "he'd"
        for i in range(len(words)):
            if words[i][-2:] == "'s" or words[i][-2:] == "s'":
                words[i] = words[i][:-2]
            elif words[i][0] == "'":
                words[i] = words[i][1:]
            elif words[i][-1] == "'":
                words[i] = words[i][:-1]
            elif words[i][-2:] == "'d":
                words[i] = words[i][:-2]

        for i in range(len(words)):
            # Replace stopwords and short words with spaces.
            
            if words[i] in stopwords:
                stops += 1 
                words[i] = ' '*len(words[i])
            elif len(words[i]) < 3:
                short += 1
                words[i] = ' '*len(words[i])
          
        outputtext.write(' '.join(words) + '\n')
    print('Preprocessing stats for {}'.format(args.input))
    print('Stopwords removed: {:>12}'.format(stops))
    print('Short words removed: {:>10}'.format(short))

    inputtext.close()
    if outputtext != sys.stdout:
        outputtext.close()


if __name__=='__main__':

    parser = argparse.ArgumentParser(description='A text preprocessor.')

    parser.add_argument('input', help='Text to process.')
    parser.add_argument('stopwords', help='Stopwords list.')
    parser.add_argument('--output', dest='output', 
            help='File for processed output.')
    args = parser.parse_args() 
    
    preprocess(args)
