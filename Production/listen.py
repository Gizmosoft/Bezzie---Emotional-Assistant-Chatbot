import pickle
import json
import random
import time
import TrueFalse, PosNeg

control = ""
## APPLY A LOOP TO LISTEN THIS 3-4 TIMES
def analysis(user_input):
    loaded_model = pickle.load(open(PosNeg.filename, 'rb'))         #SERIALIZES THE LIS/STR ETC. TO CHAR STREAM
    tag = PosNeg.model.predict([user_input]).tolist()[0]
    return tag

def happy_chatbot():
    HAPPY_INTENT = ["And?",
                    "Then?",
                    "Okay, then?"]
    return random.choice(HAPPY_INTENT)

def sad_chatbot():
    SAD_INTENT = ["Oh",
                  "Okay",
                  "Oh okay"]
    return random.choice(SAD_INTENT)

def anything_else(user_input):
    control = "confirm"
    return "It's good that you shared so much. Do you have anything else to share?", control

def confirmation(user_input):
    loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
    yesNo = TrueFalse.model.predict([user_input]).tolist()[0]
    if(user_input=="yes"):
        control = "listening2"
        return "Sure, go ahead", control
    else:
        control = "diagnose"
        return "Let me ask you some questions so that I can know better about you. Please answer them honestly with a YES or a NO.", control
        ## CONTROL NEEDS TO BE SENT TO THE DIAGNOSTICS FILE WHERE ALL DIAGNOSIS FUCNTIONS ARE PRESENT

def listening1(user_input):
    control = "listening1"
    if(analysis(user_input)=="positive"):
        return happy_chatbot(), control
    else:
        return sad_chatbot(), control

def listening2(user_input):
    control = "listening2"
    if(analysis(user_input)=="positive"):
        return happy_chatbot(), control
    else:
        return sad_chatbot(), control

def listening3(user_input):
    control = "listening3"
    if(analysis(user_input)=="positive"):
        return happy_chatbot(), control
    else:
        return sad_chatbot(), control
