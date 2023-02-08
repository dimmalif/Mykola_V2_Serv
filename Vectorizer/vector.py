from Dataset import dataset


async def vectoring(text, vectorizer, clf):
    trg = dataset.TRIGGERS.intersection(text.split())
    if not trg:
        return

    text.replace(list(trg)[0], '')
    text_vector = vectorizer.transform([text]).toarray()[0]
    answer = clf.predict([text_vector])[0]
    func_name = answer.split()[0]
    return answer, func_name

