import librosa
import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor


tokenizer = Wav2Vec2Processor.from_pretrained("/home/dmytro/Desktop/Mykola/TestRECOGNITION/Model/wav2vec2-xls-r-base-uk-with-small-lm")
model = Wav2Vec2ForCTC.from_pretrained("/home/dmytro/Desktop/Mykola/TestRECOGNITION/Model/wav2vec2-xls-r-base-uk-with-small-lm")


def recognize(file_name):
    audio, rate = librosa.load(f"{file_name}", sr=16000)
    input_values = tokenizer(audio, return_tensors="pt").input_values
    logits = model(input_values).logits
    prediction = torch.argmax(logits, dim=-1)
    transcription = tokenizer.batch_decode(prediction)[0]
    print(transcription)
    return transcription

