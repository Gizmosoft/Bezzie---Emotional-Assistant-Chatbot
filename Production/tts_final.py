from gtts import gTTS
from playsound import playsound
import os

def speak(sentence):
    v = gTTS(text=sentence,lang="en",slow=False)
    filename = "test.mp3"
    v.save(filename)
    playsound(filename)
    os.remove(filename)


# while(True):
#     speak(input())
