import TrueFalse
import pickle
import json
import random
import time
from report import *

depression_imp = {'guilt'          : 0,
                  'suicidal'       : 0}

anxiety_imp    = {'restlessness'   : 0,
                  'uneasiness'     : 0,
                  'tension'        : 0}

stress_imp     = {'relax'          : 0,
                  'energy'         : 0}

ocd_imp        = {'repetitive_thoughts'     : 0,
                  'uncontrolled_thoughts'   : 0}

depression_gen = {'interest'        : 0,
                  'concentration'   : 0,
                  'pessimism'       : 0,
                  'sleep'           : 0,
                  'appetite'        : 0}

anxiety_gen    = {'appetite'        : 0,
                  'sleep'           : 0,
                  'concentration'   : 0}

stress_gen     = {'procastination'  : 0,
                  'pessimism'       : 0,
                  'sleep'           : 0,
                  'appetite'        : 0}

ocd_gen        = {'concentration'   : 0,
                  'pessimism'       : 0,
                  'sleep'           : 0}

## ANXIETY MODULES - IMPORTANT
def restlessness(user_input):
    control = "restless"
    return "Are you experiencing restlessness and inability to relax lately?", control

def uneasiness(user_input):
    loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
    yesNo = TrueFalse.model.predict([user_input]).tolist()[0]
    if (yesNo == "yes" or user_input == "yes"):
        anxiety_imp['restlessness'] = 1
    else:
        anxiety_imp['restlessness'] = 0
    control = "uneasy"
    return "Are you experiencing uneasiness in your body physically or mentally? It may be an experience of increased heart rates, a feeling of dizziness or something else.", control

def tension(user_input):
    loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
    yesNo = TrueFalse.model.predict([user_input]).tolist()[0]
    if (yesNo == "yes" or user_input == "yes"):
        anxiety_imp['uneasiness'] = 1
    else:
        anxiety_imp['uneasiness'] = 0
    control = "tension"
    return "Is there some sort of tension you are undergoing recently?", control

def diagnosis_stage1(user_input):
    loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
    yesNo = TrueFalse.model.predict([user_input]).tolist()[0]
    if (yesNo == "yes" or user_input == "yes"):
        anxiety_imp['tension'] = 1
    else:
        anxiety_imp['tension'] = 0
    if((anxiety_imp['restlessness']+anxiety_imp['uneasiness']+anxiety_imp['tension'])<2):
        control = "diagnosis_stage1"
        ## Question of guilt - depression important
        return "Do you ever think you are guilty of the happenings around you? Do you ever feel, you are responsible for mishaps around you?", control
    else:
        control = "diagnosis_stage3"
        return "Do you feel less energetic lately?", control

def guilt(user_input):
    loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
    yesNo = TrueFalse.model.predict([user_input]).tolist()[0]
    if (yesNo == "yes" or user_input == "yes"):
        depression_imp['guilt'] = 1
    else:
        depression_imp['guilt'] = 0
    control = "guilt"
    return "Do you ever feel like hurting yourself physically or comitting suicide?", control

def diagnosis_stage2(user_input):
    loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
    yesNo = TrueFalse.model.predict([user_input]).tolist()[0]
    if (yesNo == "yes" or user_input == "yes"):
        depression_imp['suicidal'] = 1
    else:
        depression_imp['suicidal'] = 0
    if((depression_imp['guilt']+depression_imp['suicidal'])<1):
        control = "diagnosis_stage2"
        ## Question of repetitive_thoughts - ocd important
        return "Do you feel that you have repetitive thoughts very often? These thoughts may not be necessary very often but they keep popping in your head all the time and stop you from focussing elsewhere.", control
    else:
        control = "diagnosis_stage3"
        return "Do you feel less energetic lately?", control

def repetitive_thoughts(user_input):
    loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
    yesNo = TrueFalse.model.predict([user_input]).tolist()[0]
    if (yesNo == "yes" or user_input == "yes"):
        ocd_imp['repetitive_thoughts'] = 1
    else:
        ocd_imp['repetitive_thoughts'] = 0
    control = "repeats"
    #ASK ABOUT UNCONTROLLED THOUGHTS
    return "Do you feel like you have no control over your thoughts? It may be cases where the thoughts feel totally out of your control and having them causes discomfort.", control

def diagnosis_stage3(user_input):
    loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
    yesNo = TrueFalse.model.predict([user_input]).tolist()[0]
    if (yesNo == "yes" or user_input == "yes"):
        ocd_imp['uncontrolled_thoughts'] = 1
    else:
        ocd_imp['uncontrolled_thoughts'] = 0
    control = "diagnosis_stage3"
    return "Do you feel less energetic lately?", control

def energy(user_input):
    loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
    yesNo = TrueFalse.model.predict([user_input]).tolist()[0]
    if (yesNo == "yes" or user_input == "yes"):
        stress_imp['energy'] = 1
    else:
        stress_imp['energy'] = 0
    control = "energy"
    #GO TO relax
    return "Are you finding it hard to relax lately? Maybe your busy schedule or work load is burdening you.", control

def diagnosis_stage4(user_input):
    loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
    yesNo = TrueFalse.model.predict([user_input]).tolist()[0]
    if (yesNo == "yes" or user_input == "yes"):
        stress_imp['relax'] = 1
    else:
        stress_imp['relax'] = 0
    control = imp_diag_analysis()
    return "You are doing great! Just answer few more questions.", control

def imp_diag_analysis():
    if((anxiety_imp['restlessness']+anxiety_imp['uneasiness']+anxiety_imp['tension'])>=2):
        control = "anxiety_detected"
    elif((depression_imp['guilt']+depression_imp['suicidal'])>=1):
        control = "depression_detected"
    elif((ocd_imp['repetitive_thoughts']+ocd_imp['uncontrolled_thoughts'])>=1):
        control = "ocd_detected"
    else:
        control = "stress_detected"
    return control

### GENERAL ATTRIBUTES ###
def interest(user_input):
    loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
    yesNo = TrueFalse.model.predict([user_input]).tolist()[0]
    return yesNo

def concentration(user_input):
    loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
    yesNo = TrueFalse.model.predict([user_input]).tolist()[0]
    return yesNo

def pessimism(user_input):
    loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
    yesNo = TrueFalse.model.predict([user_input]).tolist()[0]
    return yesNo

def sleep(user_input):
    loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
    yesNo = TrueFalse.model.predict([user_input]).tolist()[0]
    return yesNo

def appetite(user_input):
    loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
    yesNo = TrueFalse.model.predict([user_input]).tolist()[0]
    return yesNo

def procastination(user_input):
    loaded_model = pickle.load(open(TrueFalse.filename, 'rb'))
    yesNo = TrueFalse.model.predict([user_input]).tolist()[0]
    return yesNo
#########################
# GENERAL ATTRIBUTES FUNCTIONS #
#########################
#########################
# ANXIETY GENERAL #
#########################
def anxietyGen1(user_input):
    control = "anxietyGen1"
    return "Are you facing any issues with your sleep cycle? Is there any discomfort in sleeping at night?", control

def anxietyGen2(user_input):
    yesNo = sleep(user_input)
    if(yesNo == "yes" or user_input == "yes"):
        anxiety_gen['sleep'] = 1
    else:
        anxiety_gen['sleep'] = 0
    control = "anxietyGen2"
    return "Are you having improper food habits lately? Like eating too much or too less.", control

def anxietyGen3(user_input):
    yesNo = appetite(user_input)
    if(yesNo == "yes" or user_input == "yes"):
        anxiety_gen['appetite'] = 1
    else:
        anxiety_gen['appetite'] = 0
    control = "anxietyGen3"
    return "Do you find it difficult to concentrate on your work or anything you do?", control

def anxietyGen4(user_input):
    yesNo = concentration(user_input)
    if(yesNo == "yes" or user_input == "yes"):
        anxiety_gen['concentration'] = 1
    else:
        anxiety_gen['concentration'] = 0
    control = "anxietyGen4"
    return "Bravo! Thank you for answering these questions well.", control

def diagnosed_anxiety_analysis():
    ob=analyze_anxiety(anxiety_imp, anxiety_gen, stress_imp)
    control = ob[1]
    ob=ob[0]
    return ob, control
#########################
# DEPRESSION GENERAL #
#########################
def depressionGen1(user_input):
    control = "depressionGen1"
    return "Have you been finding things less interesting these days?", control

def depressionGen2(user_input):
    yesNo = interest(user_input)
    if(yesNo == "yes" or user_input == "yes"):
        depression_gen['interest'] = 1
    else:
        depression_gen['interest'] = 0
    control = "depressionGen2"
    return "Do you find it difficult to concentrate on your work or anything you do?", control

def depressionGen3(user_input):
    yesNo = concentration(user_input)
    if(yesNo == "yes" or user_input == "yes"):
        depression_gen['concentration'] = 1
    else:
        depression_gen['concentration'] = 0
    control = "depressionGen3"
    return "Do you have any pessimistic or negative thoughts about your life by chance?", control

def depressionGen4(user_input):
    yesNo = pessimism(user_input)
    if(yesNo == "yes" or user_input == "yes"):
        depression_gen['pessimism'] = 1
    else:
        depression_gen['pessimism'] = 0
    control = "depressionGen4"
    return "Are you facing any issues with your sleep cycle? Is there any discomfort in sleeping at night?", control

def depressionGen5(user_input):
    yesNo = sleep(user_input)
    if(yesNo == "yes" or user_input == "yes"):
        depression_gen['sleep'] = 1
    else:
        depression_gen['sleep'] = 0
    control = "depressionGen5"
    return "Are you having improper food habits lately? Like eating too much or too less.", control

def depressionGen6(user_input):
    yesNo = appetite(user_input)
    if(yesNo == "yes" or user_input == "yes"):
        depression_gen['appetite'] = 1
    else:
        depression_gen['appetite'] = 0
    control = "depressionGen6"
    return "Bravo! Thank you for answering these questions well.", control

def diagnosed_depression_analysis():
    ob=analyze_depression(depression_imp, depression_gen, stress_imp)
    control = ob[1]
    ob=ob[0]
    return ob, control

#########################
# OCD GENERAL #
#########################
def ocdGen1(user_input):
    control = "ocdGen1"
    return "Do you find it difficult to concentrate on your work or anything you do?", control

def ocdGen2(user_input):
    yesNo = concentration(user_input)
    if(yesNo == "yes" or user_input == "yes"):
        ocd_gen['concentration'] = 1
    else:
        ocd_gen['concentration'] = 0
    control = "ocdGen2"
    return "Do you have any pessimistic or negative thoughts about yur life by chance?", control

def ocdGen3(user_input):
    yesNo = pessimism(user_input)
    if(yesNo == "yes" or user_input == "yes"):
        ocd_gen['pessimism'] = 1
    else:
        ocd_gen['pessimism'] = 0
    control = "ocdGen3"
    return "Are you facing any issues with your sleep cycle? Is there any discomfort in sleeping at night?", control

def ocdGen4(user_input):
    yesNo = sleep(user_input)
    if(yesNo == "yes" or user_input == "yes"):
        ocd_gen['sleep'] = 1
    else:
        ocd_gen['sleep'] = 0
    control = "ocdGen4"
    return "Bravo! Thank you for answering these questions well.", control

def diagnosed_ocd_analysis():
    ob=analyze_ocd(ocd_imp, ocd_gen, stress_imp)
    control = ob[1]
    ob=ob[0]
    return ob, control
#########################
# STRESS GENERAL #
#########################
def stressGen1(user_input):
    control = "stressGen1"
    return "Have you been procastinating or avoiding doing things a lot lately?", control

def stressGen2(user_input):
    yesNo = procastination(user_input)
    if(yesNo == "yes" or user_input == "yes"):
        stress_gen['procastination'] = 1
    else:
        stress_gen['procastination'] = 0
    control = "stressGen2"
    return "Do you have any pessimistic or negative thoughts about yur life by chance?", control

def stressGen3(user_input):
    yesNo = pessimism(user_input)
    if(yesNo == "yes" or user_input == "yes"):
        stress_gen['pessimism'] = 1
    else:
        stress_gen['pessimism'] = 0
    control = "stressGen3"
    return "Are you having trouble with your sleep cycle? Is there any discomfort in sleeping at night?", control

def stressGen4(user_input):
    yesNo = sleep(user_input)
    if(yesNo == "yes" or user_input == "yes"):
        stress_gen['sleep'] = 1
    else:
        stress_gen['sleep'] = 0
    control = "stressGen4"
    return "Are you having improper food habits lately? Like eating too much or too less.", control

def stressGen5(user_input):
    yesNo = appetite(user_input)
    if(yesNo == "yes" or user_input == "yes"):
        stress_gen['appetite'] = 1
    else:
        stress_gen['appetite'] = 0
    control = "stressGen5"
    return "Bravo! Thank you for answering these questions well.", control

def diagnosed_stress_analysis():
    ob=analyze_stress(stress_imp, stress_gen)
    control = ob[1]
    ob=ob[0]
    return ob, control


# print(tension("yes"))
