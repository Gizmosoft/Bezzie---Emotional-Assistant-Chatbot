import TrueFalse
import pickle
import json
import random
import time
import matplotlib.pyplot as plt

anxiety_matrix = [0, 0, 0, 0, 0, 0, 0]     # 0 FOR FALSE, 1 FOR True
# ['Evident Symptoms', 'Abnormality', 'Chest_Related', 'Brain', 'Tension', 'Sleep', 'Exaggeration']
class diagnose_anxiety(object):
    def primary_anxious(self):
        print("\n Are you experiencing restlessness and inability to relax ?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]

        if (yesNo == "yes"):
            anxiety_matrix[0] = 1
        else:
            anxiety_matrix[0] = 0
        ax = diagnose_anxiety()
        return ax.automatic_arousal_symptoms()
    def automatic_arousal_symptoms(self):

        print("\n Do you encounter abnormal heart rates or trembling?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]

        if (yesNo == "yes"):
            anxiety_matrix[1] = 1
        else:
            anxiety_matrix[1] = 0
        ax = diagnose_anxiety()
        return ax.chest_abdomen()

    def chest_abdomen(self):
        print("\n Have you ever experienced difficulty in breathing or chest pain?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]
        if (yesNo == "yes"):
            anxiety_matrix[2] = 1
        else:
            anxiety_matrix[2] = 0
        ax = diagnose_anxiety()
        return ax.brain()

    def brain(self):
        print("\nHave you ever felt like losing control , going dizzy out of the blue?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]
        if (yesNo == "yes"):
            anxiety_matrix[3] = 1
        else:
            anxiety_matrix[3] = 0
        ax = diagnose_anxiety()
        return ax.tension()

    def tension(self):
        print("\nHave you ever felt excessive muscle tension / pain or ache in any part of your body?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]
        if (yesNo == "yes"):
            anxiety_matrix[4] = 1
        else:
            anxiety_matrix[4] = 0
        ax = diagnose_anxiety()
        return ax.sleep()

    def sleep(self):
        print("\nDo you have difficulty going to sleep?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]
        if(yesNo == "yes"):
            anxiety_matrix[5] = 1
        else:
            anxiety_matrix[5] = 0
        ax = diagnose_anxiety()
        return ax.exagg_resp()  #pessimistic

    def exagg_resp(self):
        print("\nDo you think you over react these days or you are startled easily ?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]
        if (yesNo == "yes"):
            anxiety_matrix[6] = 1
        else:
            anxiety_matrix[6] = 0
        ax = diagnose_anxiety()
        return ax.report()


    def report(self):
        #print(anxiety_matrix)
        # print("<<REPORT GENERATED>>")
        x = ['Evident Symptoms', 'Abnormality', 'Chest_Related', 'Brain', 'Tension', 'Sleep', 'Exaggeration']
        plt.bar(x, anxiety_matrix)
        plt.savefig('anxiety_analysis.png')
        plt.show()

ax = diagnose_anxiety()
ax.primary_anxious()
