import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from pyexe.nlp_toolkit import *
from pyexe.case_file_auditor_utils import *
#from kmodes.kmodes import KModes
from sklearn.cluster import KMeans
import numpy as np

rootdir = "C:\\Users\\mkbcu\\OneDrive\\Desktop\\cases"

def Injury(folder):
    possible_injuries = []
    with open('../data/injury-types.txt', 'r') as file:
        for line in file.readlines():
            line = line.lower().strip()
            if '|' in line:
                possible_injuries += line.split('|')
            else:
                possible_injuries.append(line)


    # read in additional stop words from file
    nums = [f"{item}" for item in range(0, 2022)]
    numbers = frozenset(nums)
    with open("stop_words.txt", "r") as f:
        no_no_words = f.read().lower()
        bad_words = frozenset(no_no_words.split())
    bad_words = bad_words.union(numbers)
    stop_words = text.ENGLISH_STOP_WORDS.union(bad_words)

    folder_doc_list = folder_as_document_list(folder)

    # **detect type of injury by comparing to list of injuries and document term frequencies**
    vectorizer = CountVectorizer(stop_words=stop_words, max_features=10000)

    # X is a list containing word frequencies
    X = vectorizer.fit_transform([' '.join(folder_doc_list)]).toarray()[0]
    term_freq_pairs = zip(vectorizer.get_feature_names(), X)

    # arrange pairs in descending frequency
    term_freq_pairs = sorted(term_freq_pairs, key=lambda pair: pair[1], reverse=True)
    val = [i[0] if (i[0] in possible_injuries) else None for i in term_freq_pairs]
    return val

def findUnion(folder,method='tfidf',PHI =5000):
    #find price grouping
    groups = {0:[]}
    test = ""
    with open("../data/settlements.txt") as file:
        text = file.read()
        text = text.split("|")
        print(text)

    for case in text:
        k = case.split("-")
        val = k[0].strip()
        key = int(k[1].strip())
        print(f'{key}:{val}')
        lowest = -1
        lowest_price=0
        for price in list(groups.keys()):
            if(abs(price-int(key))<lowest or lowest==-1):
                lowest = abs(price-int(key))
                lowest_price= price
        if lowest<PHI:
            groups[lowest_price].append(val)
        else:
            groups[key]=[val]
            print(groups)

    df = pd.DataFrame()

    folders = [f.path for f in os.scandir(folder) if f.is_dir()]
    groupedVals = {}
    for bracket in list(groups.keys()):
        groupedVals[bracket] = set()
        for case in groups[bracket]:
            dir = os.path.join(folder,case)
            doc = folder_as_document_list(dir)
            #words = set(extract_keywords(doc, method)[0])
            words = set(Injury(dir))
            if len(groupedVals[bracket])==0:
                groupedVals[bracket]=words
            else:
                groupedVals[bracket].union(words)
            print(groupedVals[bracket])

    print(groups)
    print(groupedVals)


def wordCount(list_of_words,keywords):
    count = dict.fromkeys(keywords,0)
    for word in list_of_words:
        if word in keywords:
            count[word]+=1
    return count


#kmeansall(rootdir)
findUnion(rootdir)