from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import text
from nlp_toolkit import *
import os
import numpy as np
import pandas as pd


# get each case folder as one big string
rootdir="C:\\Users\\mkbcu\\OneDrive\\Desktop\\cases"
folders = [f.path for f in os.scandir(rootdir) if f.is_dir()]
docs = []
for dir in folders:
    docs.append(get_words_goodie_bag(dir))

# assemble list of stop words
nums = [f"{item}" for item in range(0, 2022)]
numbers = frozenset(nums)
with open("stop_words.txt", "r") as f:
    no_no_words = f.read()
    bad_words = frozenset(no_no_words.split())
bad_words = bad_words.union(numbers)
stop_words = text.ENGLISH_STOP_WORDS.union(bad_words)


# todo: other options include keeping union, intersection, or only keywords as regression features


# read in keywords from txt file (these will the columns / features for regression)
keywords = []
with open('../data/Key_Words.txt', 'r') as kwd_file:
    for line in kwd_file.readlines():
        keywords.append(line.strip())


# todo get price values (y for regression)


# assemble X for regression using the important as features (smallest # of features)
X = []
for case in docs:
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    # tfidf_matrix = vectorizer.fit_transform(case)
    tfidf_matrix = vectorizer.fit(case)
    case_words = vectorizer.get_feature_names()
    data_row = []

    for kwd in keywords:
        data_row.append(1 if kwd in case_words else 0)

    X.append(data_row)

# visualize with data frame
df_X = pd.DataFrame(X, columns=keywords)
df_X.index.name = 'case #'


# todo use X and y for regression
