from Dataset import dataset
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


def vectoring(text):
    vectorizer = CountVectorizer()
    # user_id = kwargs
    vectors = vectorizer.fit_transform(list(dataset.data_set.keys()))
    clf = LogisticRegression()
    clf.fit(vectors, list(dataset.data_set.values()))

    trg = dataset.TRIGGERS.intersection(text.split())
    if not trg:
        return

    text.replace(list(trg)[0], '')
    text_vector = vectorizer.transform([text]).toarray()[0]
    answer = clf.predict([text_vector])[0]
    func_name = answer.split()[0]
    return func_name, answer

