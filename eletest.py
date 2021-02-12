import sys
from case_file_auditor_utils import get_words_goodie_bag
from nlp_toolkit import *
import os
import time

args = sys.argv

# print(os.path.join(os.getcwd(), args[1]))
# print(os.path.abspath(__file__))

print("test 1")
sys.stdout.flush()

time.sleep(2)

print("test 2")
sys.stdout.flush()

print(extract_keywords(folder_as_document_list(args[1])))
# print(get_words_goodie_bag(args[1]))

sys.stdout.flush()

# instead of console, write contents to file

# todo determine how to name the output file
with open(args[2] + '\prediction-test.txt', 'w') as file:
    for concept in extract_keywords(folder_as_document_list(args[1])):
        file.write(','.join(concept) + '\n')