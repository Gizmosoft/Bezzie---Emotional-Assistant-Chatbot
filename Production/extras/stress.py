import TrueFalse
import pickle
import json
import random
import time
import matplotlib.pyplot as plt

stress_matrix = [0, 0, 0, 0, 0, 0, 0, 0]     # 0 FOR FALSE, 1 FOR True
# ['Major_Stress', 'Pessimism', 'Eating', 'Sleep', 'Procastination', 'Inebriation', 'Nausea', 'Flu']
class diagnose_stress(object):
    def major_stress(self):
        print("\n Have you been going through Major life changes , school or work related or maybe financial problems?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]

        if (yesNo == "yes"):
            stress_matrix[0] = 1
        else:
            stress_matrix[0] = 0
        st = diagnose_stress()
        return st.pessimistic()
    def pessimistic(self):

        print("\n Have you been pessimistic about life generally in recent times?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]

        if (yesNo == "yes"):
            stress_matrix[1] = 1
        else:
            stress_matrix[1] = 0
        st = diagnose_stress()
        return st.eating()

    def eating(self):
        print("\n Are your eating habits erratic?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]
        if (yesNo == "yes"):
            stress_matrix[2] = 1
        else:
            stress_matrix[2] = 0
        st = diagnose_stress()
        return st.sleep()

    def sleep(self):
        print("\n What about your sleeping cycles? Normal?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]
        if (yesNo == "yes"):
            stress_matrix[3] = 1
        else:
            stress_matrix[3] = 0
        st = diagnose_stress()
        return st.procas()

    def procas(self):
        print("\n Have you been procastinating a lot lately ?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]
        if (yesNo == "yes"):
            stress_matrix[4] = 1
        else:
            stress_matrix[4] = 0
        st = diagnose_stress()
        return st.inebriation()

    def inebriation(self):
        print("\n Are you using inebriative substances like alcohol or cigarettes to calm down?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]
        if(yesNo == "yes"):
            stress_matrix[5] = 1
        else:
            stress_matrix[5] = 0
        st = diagnose_stress()
        return st.nausea()

    def nausea(self):
        print("\n Are you experiencing nausea or dizziness more often recently?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]
        if (yesNo == "yes"):
            stress_matrix[6] = 1
        else:
            stress_matrix[6] = 0
        st = diagnose_stress()
        return st.flu()

    def flu(self):
        print("\n Are you suffering from cold or flu more freuqently these days?")
        response = input()
        loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
        yesNo = TrueFalse.model.predict([response]).tolist()[0]
        if(yesNo == "yes"):
            stress_matrix[7] = 1
        else:
            stress_matrix[7] = 0
        st = diagnose_stress()
        return st.report()


    def report(self):
        #print(anxiety_matrix)
        # print("<<REPORT GENERATED>>")
        x = ['Major_Stress', 'Pessimism', 'Eating', 'Sleep', 'Procastination', 'Inebriation', 'Nausea', 'Flu']
        plt.bar(x, stress_matrix)
        plt.savefig('stress_analysis.png')
        plt.show()

st = diagnose_stress()
st.major_stress()
