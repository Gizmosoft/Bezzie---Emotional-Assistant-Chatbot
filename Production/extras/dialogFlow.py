import PosNeg
import pickle
import json
import random
import time

class EmotionalAssistant(object):
    def welcome(self):
        WELCOME_INTENT = ["Hey! You look nice. Can I know how do you feel today?\n",
                          "Hi! How do you feel friend?\n",
                          "Hey! Is there anything you would want to share with me?\n",
                          "Hey there, your face says that you have something to share with me. Good or bad, I'm up for anything!\n"]
        # PRINT THE WELCOME INTENT
        print(random.choice(WELCOME_INTENT))
        # TAKE USER INPUT FOR THE WELCOME INTENT
        response = input()
        print("\nSo what is it that you want to tell me?\n")
        fu = EmotionalAssistant()
        return fu.follow_up()

    def follow_up(self):
        response = input()
        loaded_model = pickle.load(open(PosNeg.filename, 'rb'))
        tag = PosNeg.model.predict([response]).tolist()[0]
        print(tag)
        if (tag == "positive"):
    # pos += 1
            print("\nThat sounds amazing! Tell me more about it!\n")
            time.sleep(2)
            print("\n<---- take all inputs from user ----->")
        else:
    # neg +=1
            print("\nOh that's sad. Do you want to share more about it?\n")
            time.sleep(2)
            # print("\n<---- take all inputs from user ----->\n")

        rm = EmotionalAssistant()
        return rm.response_model(tag)

    def response_model(self, tag):
        if tag == "positive":
            time.sleep(2)
            print("\nI'm very happy for you that things have been going well for you lately. All the very best for you!\n")
        else:
            time.sleep(2)
            print("\nThere is always sunshine after rain. All you need is to wait for the better time to arrive. I know you are strong and will come out of this. I hope you know that I'm there for you always, no matter what.\n")
        time.sleep(1)
        return "\n<----- GO TO SPECIFIC QUESTION MODULES AND FILL OUT THE ARRAY FOR ANALYSIS ----->\n"
ea = EmotionalAssistant()
print(ea.welcome())
