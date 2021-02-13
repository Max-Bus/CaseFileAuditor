import sys
from case_file_auditor_utils import get_words_goodie_bag
from nlp_toolkit import *
import os
import time
import traceback

args = sys.argv

# print(os.path.join(os.getcwd(), args[1]))
# print(os.path.abspath(__file__))

print("test 1")
sys.stdout.flush()

time.sleep(2)

print("test 2")

# print(extract_keywords(folder_as_document_list(args[1])))
# print(get_words_goodie_bag(args[1]))

# instead of console, write contents to file

# todo determine how to name the output file
try:
    with open(args[2] + '\prediction-test.txt', 'w') as file:
        for concept in extract_keywords(folder_as_document_list(args[1])):
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
