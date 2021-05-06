import sys
from case_file_auditor_utils import *
from nlp_toolkit import *
import os
import time
import traceback
import re
import pandas as pd
import docx
from sklearn.feature_extraction.text import CountVectorizer

args = sys.argv

# print(os.path.join(os.getcwd(), args[1]))
# print(os.path.abspath(__file__))

# print(args[1])
# sys.stdout.flush()

print("test 1")
sys.stdout.flush()

# read in injury types from file
try:
    # read in injury words
    possible_injuries = []
    with open('data/injury-types.txt', 'r') as file:
        for line in file.readlines():
            line = line.lower().strip()
            if '|' in line:
                possible_injuries += line.split('|')
            else:
                possible_injuries.append(line)

    # read in medical words
    medical_words = []
    with open('data/medical-words.txt', 'r') as file:
        for line in file.readlines():
            line = line.lower().strip()
            if '|' in line:
                medical_words += line.split('|')
            else:
                medical_words.append(line)

    # read in injury adjectives
    injury_adjectives = []
    with open('data/injury-adjectives.txt', 'r') as file:
        for line in file.readlines():
            line = line.lower().strip()
            if '|' in line:
                injury_adjectives += line.split('|')
            else:
                injury_adjectives.append(line)

    print('test2')
    sys.stdout.flush()

    # read in additional stop words from file
    nums = [f"{item}" for item in range(0, 2022)]
    numbers = frozenset(nums)
    with open("pyexe/stop_words.txt", "r") as f:
        no_no_words = f.read().lower()
        bad_words = frozenset(no_no_words.split())
    bad_words = bad_words.union(numbers)
    stop_words = text.ENGLISH_STOP_WORDS.union(bad_words)

    # todo determine how to name the output file
    with open(args[2] + '/prediction-test.txt', 'w') as file:
        folder_doc_list, pdf_list = folder_as_document_list(args[1])

        # tfidf extracted keywords
        for concept in extract_keywords(folder_doc_list):
            file.write(', '.join(concept) + '\n')

        file.write('\n')

        # count extracted keywords
        for concept in extract_keywords(folder_doc_list, 'count'):
            file.write(','.join(concept) + '\n')

        if (len(pdf_list) > 0):
            file.write("pdf files are not supported by this program. here are the files that were overlooked:\n")
            for pdf in pdf_list:
                file.write(pdf + "\n")
            file.write('\n')

        # ****************************************************************************************
        # **detect type of injury by comparing to list of injuries and document term frequencies**
        # ****************************************************************************************

        vectorizer = CountVectorizer(stop_words=stop_words, max_features=10000)

        # X is a list containing word frequencies
        X = vectorizer.fit_transform([' '.join(folder_doc_list)]).toarray()[0]
        term_freq_pairs = zip(vectorizer.get_feature_names(), X)

        # arrange pairs in descending frequency
        term_freq_pairs = sorted(term_freq_pairs, key=lambda pair: pair[1], reverse=True)

        # print out the detected injury words and their frequencies
        file.write('\nwords potentially related to the injury:\n')
        for word, freq in term_freq_pairs:
            if word in possible_injuries:
                file.write(f'{word:<25} ({freq:<3d} occurrences)\n')

        # print out detected injury adjectives and their frequencies
        file.write('\nwords that potentially describe the nature of the injury:\n')
        for word, freq in term_freq_pairs:
            if word in injury_adjectives:
                file.write(f'{word:<25} ({freq:<3d} occurrences)\n')

        # print out possible treatments or medical procedures that might be needed or were done
        file.write('\nwords potentially related to medical attention and treatment:\n')
        for word, freq in term_freq_pairs:
            if word in medical_words:
                file.write(f'{word:<25} ({freq:<3d} occurrences)\n')

    # print file contents so that it can be put in mini display on console
    with open(args[2] + '/prediction-test.txt', 'r') as file:
        # print(file.read())
        text = file.read().replace('\n', '<br>').replace(' ', '&nbsp;')
        print(text)


except Exception as e:
    # Just print(e) is cleaner and more likely what you want,
    # but if you insist on printing message specifically whenever possible...
    # if hasattr(e, 'message'):
    #     print(e.message)
    # else:
    #     print(e)

    print(traceback.format_exc())

sys.stdout.flush()