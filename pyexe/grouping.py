import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from pyexe.nlp_toolkit import *
from pyexe.case_file_auditor_utils import *
from kmodes.kmodes import KModes
from sklearn.cluster import KMeans
import numpy as np

rootdir = "C:\\Users\\mkbcu\\OneDrive\\Desktop\\cases"
def kmodes(folder,method='tfidf'):
    df = pd.DataFrame()

    folders = [f.path for f in os.scandir(folder) if f.is_dir()]

    for dir in folders:
        doc = folder_as_document_list(dir)
        df[dir] = extract_keywords(doc, method)[0]

    km = KModes(n_clusters=6, init='Huang', n_init=5, verbose=0)
    df = df.T

    clusters = km.fit_predict(df)
    print(km.cluster_centroids_)
    print(clusters)

def wordCount(list_of_words,keywords):
    count = dict.fromkeys(keywords,0)
    for word in list_of_words:
        if word in keywords:
            count[word]+=1
    return count

#find most common words in all of the files and use kmeans from each folder to group them
def kmeansall(folder,method='tfidf'):
    df = pd.DataFrame()

    doc = folder_as_document_list(folder)
    words = extract_keywords(doc, method)[0]
    #first find most common words total
    folders = [f.path for f in os.scandir(folder) if f.is_dir()]
    for dir in folders:
        docs = get_words_goodie_bag(dir).split()
        count = wordCount(docs, words)
        df = df.append(count,ignore_index = True)

    km = KMeans(n_clusters=6, random_state=0)
    groups=km.fit_predict(df)
    print(km.cluster_centers_)
    print(groups)

#kmeansall(rootdir)
kmodes(rootdir)