from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import text
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression, Lasso
from pyexe.nlp_toolkit import *
from pyexe.case_file_auditor_utils import *
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
y=[]
with open('../data/settlements.txt') as f:
    vals = f.read().split("|")
    print(vals)
    y = [int(i.split("-")[1].strip()) for i in vals]
    y = np.asarray(y)

# assemble X for regression using the important as features (smallest # of features)
X = []
#vectorizer = TfidfVectorizer(stop_words=stop_words)
#tfidf_matrix = vectorizer.fit_transform(docs)
#tfidf_matrix = vectorizer.fit(case)
#case_words = vectorizer.get_feature_names()
for case in docs:
    data_row = []
    for kwd in keywords:
        data_row.append(1 if kwd in case else 0)
    X.append(data_row)

# visualize with data frame
df_X = pd.DataFrame(X, columns=keywords)
df_X.index.name = 'case #'


# todo use X and y for regression
print(X)
print(y)
print(y.T)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.4, random_state = 3054)
reg = LinearRegression()
cv_scores = cross_val_score(reg, X, y, cv=5)
print("CV Scores: {}".format(cv_scores))
print("CV Score Mean: {}".format(np.mean(cv_scores)))

# use X and y for lasso
lasso = Lasso(normalize = True, alpha = 0.1)
lasso.fit(X_train, y_train)
print("Lasso Coefs: {}".format(lasso.coef_))
print("Lasso Scores: {}".format(lasso.score(X_test, y_test)))
