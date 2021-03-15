from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction import text

from sklearn.decomposition import TruncatedSVD
from pyexe.case_file_auditor_utils import *


def extract_keywords(documents, method='tfidf'):
    nums = [f"{item}" for item in range(0, 2022)]
    numbers=frozenset(nums)
    with open("stop_words.txt", "r") as f:
        no_no_words=f.read()
        bad_words = frozenset(no_no_words.split())
    bad_words= bad_words.union(numbers)
    stop_words = text.ENGLISH_STOP_WORDS.union(bad_words)
    vectorizer = None

    if method == 'tfidf':
        vectorizer = TfidfVectorizer(stop_words=stop_words)

    elif method == 'count':
        vectorizer = CountVectorizer(stop_words=stop_words)

    X = vectorizer.fit_transform(documents)

    # LSA
    lsa = TruncatedSVD(n_components=2, n_iter=50)
    lsa.fit(X)

    # get important words
    terms = vectorizer.get_feature_names()
    concept_keywords = []
    for i, comp in enumerate(lsa.components_):
        term_importance_pairs = zip(terms, comp)
        sorted_terms = sorted(term_importance_pairs, key=lambda x: x[1], reverse=True)[:7]

        ls = []
        for kwd in sorted_terms:
            ls.append(kwd[0])

        concept_keywords.append(ls)

    # for i, concept in enumerate(concept_keywords):
    #     print('concept {}: {}'.format(i + 1, concept))

    return concept_keywords

#documents = read_file_contents('test_folder/zang.txt').split('    ')
#print(extract_keywords(documents=documents))
