from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from case_file_auditor_utils import *


def extract_keywords(documents):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(documents)

    # LSA
    lsa = TruncatedSVD(n_components=2, n_iter=50)
    lsa.fit(X)

    # get important words
    terms = vectorizer.get_feature_names()
    concept_keywords = []
    for i, comp in enumerate(lsa.components_):
        termp_importance_pairs = zip(terms, comp)
        sorted_terms = sorted(termp_importance_pairs, key=lambda x: x[1], reverse=True)[:7]

        ls = []
        for kwd in sorted_terms:
            ls.append(kwd[0])

        concept_keywords.append(ls)

    # for i, concept in enumerate(concept_keywords):
    #     print('concept {}: {}'.format(i + 1, concept))

    return concept_keywords

# documents = read_file_contents('test_folder/zang.txt').split('    ')
# print(extract_keywords(documents=documents))
