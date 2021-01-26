import sys
from case_file_auditor_utils import *
import os

print('Hello from Python!')
args = sys.argv
# print(os.path.join(os.getcwd(), args[1]))
# print(os.path.abspath(__file__))
print(get_words_goodie_bag(args[1]))

sys.stdout.flush()