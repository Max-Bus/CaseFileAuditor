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

# todo determine how to name the output file
try:
    with open(args[2] + '\prediction-test.txt', 'w') as file:
        for concept in extract_keywords(folder_as_document_list(args[1])):
            file.write(','.join(concept) + '\n')

        file.write('\n')
        for concept in extract_keywords(folder_as_document_list(args[1]), 'count'):
            file.write(','.join(concept) + '\n')

except Exception as e:
    # Just print(e) is cleaner and more likely what you want,
    # but if you insist on printing message specifically whenever possible...
    # if hasattr(e, 'message'):
    #     print(e.message)
    # else:
    #     print(e)

    print(traceback.format_exc())

sys.stdout.flush()