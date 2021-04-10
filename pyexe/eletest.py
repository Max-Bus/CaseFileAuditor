import sys
from case_file_auditor_utils import *
from nlp_toolkit import *
import os
import time
import traceback
import re
import pandas as pd
import docx

args = sys.argv

# print(os.path.join(os.getcwd(), args[1]))
# print(os.path.abspath(__file__))

print(args[1])
sys.stdout.flush()

print("test 1")
sys.stdout.flush()

# time.sleep(5)

print("test 2")

# print(extract_keywords(folder_as_document_list(args[0])))
# print(get_words_goodie_bag(args[0]))

# instead of console, write contents to file

# read in injury types from file
possible_injuries = []
with open('../data/injury-types.txt', 'r') as file:
    for categ in file.read().lower().split(';'):
        if '|' in categ:
            possible_injuries += categ.split('|')
        else:
            possible_injuries += categ

# store injury words and their frequency to rank by importance
potential_key_words = dict(zip(possible_injuries, [0 for i in range(len(possible_injuries))]))

# todo determine how to name the output file
try:
    with open(args[2] + '\prediction-test.txt', 'w') as file:
        folder_doc_list = folder_as_document_list(args[1])

        # look for injury type words and store counts
        for docs in folder_doc_list:
            docs = docs.lower()
            for word in docs.split():
                if word in possible_injuries:
                    potential_key_words[word] = potential_key_words[word] + 1

        for concept in extract_keywords(folder_doc_list):
            file.write(','.join(concept) + '\n')

        file.write('\n')
        for concept in extract_keywords(folder_doc_list, 'count'):
            file.write(','.join(concept) + '\n')


        file.write('\n')
        file.write('The following words may describe and/or are related to the injury:\n')

        sorted_frequencies = {key : val for key, val in sorted(potential_key_words.items(), key=lambda item: item[1])}
        for key, value in sorted_frequencies.items():
            file.write(f'{key}: {value} occurrences\n')


except Exception as e:
    # Just print(e) is cleaner and more likely what you want,
    # but if you insist on printing message specifically whenever possible...
    # if hasattr(e, 'message'):
    #     print(e.message)
    # else:
    #     print(e)

    print(traceback.format_exc())

sys.stdout.flush()