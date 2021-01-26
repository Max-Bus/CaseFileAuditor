import sys
from case_file_auditor_utils import get_words_goodie_bag
import os

args = sys.argv
# print('Hello from Python! + ' + args[1])
# sys.stdout.flush()

# print(os.path.join(os.getcwd(), args[1]))
# print(os.path.abspath(__file__))
print(len(get_words_goodie_bag(args[1])))

sys.stdout.flush()