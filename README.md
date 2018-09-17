## Description:
This project will take you through a simplified workflow of preparing and
indexing text in preparation for more comprehensive analysis. First, it
pre-processes any given text file in the preprocessor, and then perform
indexing of the unique words using a map data structure.

## Dependencies:
- avl_tree.py
- unsorted_table_map.py
- sorted_table_map.py
- chain_hash_map.py
- probe_hash_map.py
- splay_tree.py
- red_black_tree.py
- binary_search_tree.py
- binary_tree.py
- Empty.py
- hash_map_base.py
- linked_binary_tree.py
- linked_queue.py
- map_base.py
- tree.py

## Original:
- project4.py
- preprocessor.py
- Indexer.py

## Requirements:
- Python 3

## Imported modules:
- time
- collections
- argparse
- sys

## Needed Input files:
- original text
- preprocessed text
- optional typeofMap
- optional indexFile (for indexed output)

## Run as:
- python3 project4.py [-h] [--map MAP] [--index INDEX] original preprocessed
- python3 preprocessor.py [-h] [--output OUTPUT] input stopwords

## Operation:
In the User Interface (UI), to show the user, the stats would be printed out
like how much time a particular map took for indexing, how many words were
indexed, average word frequency, median word frequency etc. At the end of
which, in the prompt, user would be asked if they want to search for a word.
If the word is not found, the user would be asked to input a new search word.
And if the word is found, all the original lines containing that word would be
printed, including the stats like, how much time it took for lookup, and
the total occurrence of that word. After which, user is asked if they want to
quit (or continue searching a new word). If no, then search is performed,
while yes would exit.

## Output:
To write an index file of all the words is an optional argument, while if
asked to make one, a new index file of whatever name user gave would be
written. The format of which would be the words (key/unique word) as the
first word on each line followed by the line numbers of where those words
occurred (values).

