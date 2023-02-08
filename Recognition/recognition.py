import librosa
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
from Vectorizer.vector import *
# from Bot_Mykola.init import clf, vectorizer
# from Detectaig_command.detect_and_run import run
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from Dataset import dataset

path_low ='/home/dmytro/Desktop/Mykola/TestRECOGNITION/Model/wav2vec2-xls-r-base-uk-with-small-lm'
path_midl = '/home/dmytro/Desktop/wav2vec2-xls-r-300m-uk-with-news-lm'

tokenizer = Wav2Vec2Processor.from_pretrained(path_midl)
model = Wav2Vec2ForCTC.from_pretrained(path_midl)



# def recognize(file_name):
#     audio, rate = librosa.load(f"{file_name}", sr=16000)
#     input_values = tokenizer(audio, return_tensors="pt").input_values
#     logits = model(input_values).logits
#     prediction = torch.argmax(logits, dim=-1)
#     transcription = tokenizer.batch_decode(prediction)[0]
#     print(transcription)
#     ans, f_name = vectoring(transcription, vectorizer, clf)
#     run(file_name)
#     return transcription, ans, f_name


def init_recogn():
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(list(dataset.data_set.keys()))
    clf = LogisticRegression()
    clf.fit(vectors, list(dataset.data_set.values()))

# ---------------------------------------------------------------
import librosa
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

PATH_LOW = '/home/dmytro/Desktop/Mykola/TestRECOGNITION/Model/wav2vec2-xls-r-base-uk-with-small-lm'
PATH_MIDL = '/home/dmytro/Desktop/wav2vec2-xls-r-300m-uk-with-news-lm'

TOKENIZER = Wav2Vec2Processor.from_pretrained(PATH_MIDL)
MODEL = Wav2Vec2ForCTC.from_pretrained(PATH_MIDL)


class Recognition:
    def __init__(self, f_name):
        self.f_name = f_name
        self.audio, self.rate = librosa.load(f"{f_name}", sr=16000)
        self.input_values = TOKENIZER(self.audio, return_tensors="pt").input_values

        self.logits = MODEL(self.input_values).logits
        self.prediction = torch.argmax(self.logits, dim=-1)

    def recognise(self):
        transcription = TOKENIZER.batch_decode(self.prediction)[0]
        return transcription

    