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

sys.stdout.flush()