import TrueFalse
import pickle
import json
import random
import time
import matplotlib.pyplot as plt

ocd_matrix = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]     # 0 FOR FALSE, 1 FOR True
# ['Anxious', 'Fear', 'Constant_Check', 'Crazy Thoughts', 'Useless', 'Unnecessary Repeats', 'Right Feeling', 'Worrisome','Unwanted Thoughts','Thought Control']
class diagnose_ocd(object):
    def anxiety(self):
        print("\n Do you ever experience repetitive thoughts that cause you anxiety?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]

        if (yesNo == "yes"):
            ocd_matrix[0] = 1
        else:
            ocd_matrix[0] = 0
        ocd = diagnose_ocd()
        return ocd.fear()
    def fear(self):
        
        print("\n Do you ever fear germs or engage in excessive cleaning?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]

        if (yesNo == "yes"):
            ocd_matrix[1] = 1
        else:
            ocd_matrix[1] = 0
        ocd=diagnose_ocd()
        return ocd.constant_check()

    def constant_check(self):
        print("\n Do you experience the need to constantly check on something or arrange things?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]
        if (yesNo == "yes"):
            ocd_matrix[2] = 1
        else:
            ocd_matrix[2] = 0
        ocd=diagnose_ocd()
        return ocd.crazy_thoughts()

    def crazy_thoughts(self):
        print("\nDo you worry about acting on a senseless urge, like pushing a stranger in front of a bus or stabbing a loved one with a knife?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]
        if (yesNo == "yes"):
            ocd_matrix[3] = 1
        else:
            ocd_matrix[3] = 0
        ocd=diagnose_ocd()
        return ocd.useless()

    def useless(self):
        print("\nDo you collect “useless” objects, or inspect the trash before it gets thrown out to see if you missed something?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]
        if (yesNo == "yes"):
            ocd_matrix[4] = 1
        else:
            ocd_matrix[4] = 0
        ocd=diagnose_ocd()
        return ocd.unnecessary_repeat()

    def unnecessary_repeat(self):
        print("\nDo you unnecessarily re-read letters, emails, or text messages before or after you’ve sent them?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]
        if(yesNo == "yes"):
            ocd_matrix[5] = 1
        else:
            ocd_matrix[5] = 0
        ocd=diagnose_ocd()
        return ocd.feels_right()

    def feels_right(self):
        print("\nDo you repeat routine actions like opening a door, putting on a shoe, or getting into bed over and over until it feels right?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]
        if (yesNo == "yes"):
            ocd_matrix[6] = 1
        else:
            ocd_matrix[6] = 0
        ocd=diagnose_ocd()
        return ocd.worry()

    def worry(self):
        print("\nDo you excessively worry about things like fires, car accidents, or your house getting flooded?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]
        if (yesNo == "yes"):
            ocd_matrix[7] = 1
        else:
            ocd_matrix[7] = 0
        ocd=diagnose_ocd()
        return ocd.unwanted_thoughts()
    

    def unwanted_thoughts(self):
        print("\nDo you suffer from unwanted thoughts and mental images inlcuding ones that are sexually explicit or violent?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]
        if (yesNo == "yes"):
            ocd_matrix[8] = 1
        else:
            ocd_matrix[8] = 0
        ocd=diagnose_ocd()
        return ocd.thought_control()

    def thought_control(self):
        print("\nDo you struggle to control obsessive thoughts or compulsive behaviors?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]
        if (yesNo == "yes"):
            ocd_matrix[9] = 1
        else:
            ocd_matrix[9] = 0
        ocd=diagnose_ocd()
        return ocd.report()
    
    
    
    def report(self):
        #print(ocd_matrix)
        # print("<<REPORT GENERATED>>")
        x =['Anxious', 'Fear', 'Constant_Check', 'Crazy Thoughts', 'Useless', 'Unnecessary Repeats', 'Right Feeling', 'Worrisome','Unwanted Thoughts','Thought Control']
        plt.pie(x, ocd_matrix)
        plt.savefig('ocd_analysis.png')
        plt.show()

ocd=diagnose_ocd()
ocd.anxiety()
