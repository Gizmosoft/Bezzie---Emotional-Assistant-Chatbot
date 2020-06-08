import TrueFalse
import pickle
import json
import random
import time
import matplotlib.pyplot as plt
 
depression_matrix = [0, 0, 0, 0, 0, 0, 0, 0, 0]     # 0 FOR FALSE, 1 FOR True
# ['interest', 'energy', 'conc', 'confidence', 'guilt', 'pessimistic', 'sleep', 'appetite', 'suicidal']
class DepressionChecker(object):
    def interest(self):
        print("\nHave you been finding things less interesting these days?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]

        if (yesNo == "yes"):
            depression_matrix[0] = 1
        else:
            depression_matrix[0] = 0
        dc = DepressionChecker()
        return dc.energy()

    def energy(self):
        print("\nDo you feel less energetic lately?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]
        if (yesNo == "yes"):
            depression_matrix[1] = 1
        else:
            depression_matrix[1] = 0
        dc = DepressionChecker()
        return dc.conc()

    def conc(self):
        print("\nDo you find it difficult to concentrate on your work or anything you do?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]
        if (yesNo == "yes"):
            depression_matrix[2] = 1
        else:
            depression_matrix[2] = 0
        dc = DepressionChecker()
        return dc.confidence()

    def confidence(self):
        print("\nIs there any lack of confidence? Do you feel less confident to do things on your own?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]
        if (yesNo == "yes"):
            depression_matrix[3] = 1
        else:
            depression_matrix[3] = 0
        dc = DepressionChecker()
        return dc.guilt()

    def guilt(self):
        print("\nDo you think you are guilty of the happenings around you? Do you ever feel, you are responsible for mishaps around you?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]
        if(yesNo == "yes"):
            depression_matrix[4] = 1
        else:
            depression_matrix[4] = 0
        dc = DepressionChecker()
        return dc.pessimistic()

    def pessimistic(self):
        print("\nWhat do you think about your future? Do you have any negative thoughts by chance?")
        response = input()
        ## new model
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]
        if (yesNo == "yes"):
            depression_matrix[5] = 1
        else:
            depression_matrix[5] = 0
        dc = DepressionChecker()
        return dc.sleep()

    def sleep(self):
        print("\nAre you facing any issues with your sleep cycle? Is there any discomfort in sleeping at night?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]
        if(yesNo == "yes"):
            depression_matrix[6] = 1
        else:
            depression_matrix[6] = 0
        dc = DepressionChecker()
        return dc.appetite()

    def appetite(self):
        print("\nWhat about the appetite these days? Are you eating too less or too much?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]
        if(yesNo == "yes"):
            depression_matrix[7] = 1
        else:
            depression_matrix[7] = 0
        dc = DepressionChecker()
        return dc.suicidal()

    def suicidal(self):
        print("\nDo you ever feel like hurting yourself physically?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]
        if(yesNo == "yes"):
            depression_matrix[8] = 1
        else:
            depression_matrix[8] = 0
        dc = DepressionChecker()
        return dc.report()

    def report(self):
        print(depression_matrix)
        # print("<<REPORT GENERATED>>")
        x = ['interest', 'energy', 'concentration', 'confidence', 'guilt', 'pessimistic', 'sleep', 'appetite', 'suicidal']
        plt.bar(x, depression_matrix)
        plt.ylabel('Attributes')
        plt.xlabel('Score')
        plt.show()

dc = DepressionChecker()
dc.interest()
