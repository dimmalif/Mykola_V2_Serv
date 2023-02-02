import sounddevice as sd
import Dataset.dataset
import os

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

from live_asr import LiveWav2Vec2
# from scripts.skills import *
# from scripts.voice import speak


#model = 'C:/Mykola_V1/models/wav2vec2-xls-r-300m-uk-with-small-lm-noisy'
model = 'C:/Users/Dmytro/Desktop/Mykola_V1/bin/wav2vec2-xls-r-300m-uk-with-wiki-lm'
asr = LiveWav2Vec2(model, device_name="default")
asr.start()


def recognize(text, vectorizer, clf):  # Convert audio ot text
    trg = words.TRIGGERS.intersection(text.split())  # Trigger word
    if not trg:
        return

    text.replace(list(trg)[0], '')  # Delete TW from data string
    text_vector = vectorizer.transform([text]).toarray()[0]
    answer = clf.predict([text_vector])[0]  # Searching answer from data_set
    func_name = answer.split()[0]  # Definition the name of function
    speak(answer.replace(func_name, ''))
    exec(func_name + '(text)')  # Association function name with data in parameters


def current_data(vectorizer, clf):
    while True:
        while True:
            text, sample_length, inference_time, confidence = asr.get_last_text()
            print(text)
            recognize(text, vectorizer, clf)


def main():
    # arduino_control.connect_to_arduino()
    speak('Сал+ам попол+ам')
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(words.data_set.keys()))
    clf = LogisticRegression()
    clf.fit(vectors, list(words.data_set.values()))

    del words.data_set

    while True:
        current_data(vectorizer, clf)


if __name__ == '__main__':
    main()

