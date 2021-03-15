import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from pyexe.nlp_toolkit import *
from pyexe.case_file_auditor_utils import *
import numpy as np


# todo: generate list of paths to folders and put in 'other_docs'
# compare all cases to all cases
rootdir="C:\\Users\\mkbcu\\OneDrive\\Desktop\\cases"
folders = [f.path for f in os.scandir(rootdir) if f.is_dir()]
print (folders)
other_docs = []
for dir in folders:
    docs = folder_as_document_list(dir)
    combined_docs = ' '.join(docs)
    other_docs.append(combined_docs)

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(other_docs)

df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names())

# key: case number str; value: list of other related cases
related_cases = {}
multi_tfidf = df.to_numpy()

# associate cases
# ith row and jth column contains "similarity" score for the ith document on the left and jth column on the right
for index, row in enumerate(np.dot(multi_tfidf, multi_tfidf.T)):

    most_relevant_indices = []
    for thing in sorted(row, reverse=True)[:3]:
        if thing > 0:
            most_relevant_indices.append(row.tolist().index(thing))

    related_cases[str(index + 1)] = np.asarray(most_relevant_indices) + 1

for key in related_cases.keys():
    val = related_cases[key].tolist()

    if int(key) in val:
        val.remove(int(key))

    related_cases[key] = list(sorted(val))

print(related_cases)

