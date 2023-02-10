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

    