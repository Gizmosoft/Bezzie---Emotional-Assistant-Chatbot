import pickle
import json
import random
import time
import TrueFalse, PosNeg
from tts_final import *
from nltk_model import *

control = ""
def welcome():
    WELCOME_INTENT = ["Hey! I'm Bezzie. Bezzie, the Chatbot!",
                      "Hi! I'm Bezzie. Bezzie, the Chatbot!",
                      "Hey there, I'm Bezzie. Bezzie, the Chatbot!"]
    control = "welcome"
    return random.choice(WELCOME_INTENT), control

def goodbye():
    GOODBYE_INTENT = ["See you later!",
                      "Bye, have a good time."]
    control = "default"
    return random.choice(GOODBYE_INTENT), control

def end():
    return "Okay, no problem! If you ever feel like talking to me, I'll be right here. Bye!"

# def init_conv_handler(user_input):      ## INTERACTION WITH THE NLTK_MODEL
#     if(user_input!="bye"):
#         return speak(bezzie_chat(user_input))
#     else:
#         return speak(goodbye())

def chatbot_controller():
    control = "chatbot"
    return "Mind if I ask you, how are you feeling right now?", control

def how_do_you_feel(user_input):
    ## ML MODEL NEEDS TO BE FED WITH LOTS OF MORE DATA
    loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
    yesNo = TrueFalse.model.predict([user_input]).tolist()[0]
    loaded_model = pickle.load(open(PosNeg.filename, 'rb'))         #SERIALIZES THE LIS/STR ETC. TO CHAR STREAM
    tag = PosNeg.model.predict([user_input]).tolist()[0]
    if (yesNo == "yes" or tag == "positive" or tag == "negative"):
        control = "permission"
        return "Can you tell me more about how do you feel?", control
    else:
        control = "welcome"
        return end(), control
