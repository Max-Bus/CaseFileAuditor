import sys
from case_file_auditor_utils import get_words_goodie_bag
from nlp_toolkit import *
import os

args = sys.argv
# print('Hello from Python! + ' + args[1])
# sys.stdout.flush()

# print(os.path.join(os.getcwd(), args[1]))
# print(os.path.abspath(__file__))
print(extract_keywords(folder_as_document_list(args[1])))

sys.stdout.flush()