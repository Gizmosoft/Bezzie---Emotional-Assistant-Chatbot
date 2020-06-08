import matplotlib.pyplot as plt
from email_module import *
import os

def generate_report(input_dictionary):
    lists = sorted(input_dictionary.items()) # sorted by key, return a list of tuples
    x, y = zip(*lists) # unpack a list of pairs into two tuples

    plt.bar(x, y)
    plt.ylabel('Score')
    plt.xlabel('Attributes')
    plt.title('Diagnosis Report')
    plt.tick_params(axis='x', which='major', labelsize=6)
    report_filename = 'diagnosis_report.png'
    if os.path.exists(report_filename):
        os.remove(report_filename)
    plt.savefig(report_filename, figsize=(6,3)  , dpi=200)
    send_email(report_filename)
    # plt.show()  # remove

def analyze_anxiety(a_dict, b_dict, c_dict):
    final_dict = dictionary_generator(a_dict, b_dict, c_dict)
    generate_report(final_dict)
    ctl = "analysis_done"
    return "From what I have studied, it looks like you are having some anxiety issues. The best thing is, sharing that would help you come out of that soon. Remember that it is just a phase and not an illness.\nAs a friend, I would suggest you to indulge into Meditation and Yoga. As the weather is also great in the evenings and early morning, head out for a long walk. That will take care of proper blood circulation in you body.\nOn a side note, if you are free sometime, do watch The Pursuit of Happyness. You will love it!", ctl

def analyze_depression(a_dict, b_dict, c_dict):
    final_dict = dictionary_generator(a_dict, b_dict, c_dict)
    generate_report(final_dict)
    ctl = "analysis_done"
    return "From what I have studied, it looks like you are a bit depressed. As a friend, I am concerned about your well-being, I would advice you to consult a counsellor or talk to your doctor.\nI would like to remind you that there is nothing to be worried of. You can come out of this. Remember, its just a phase and not a disease.\nTry indulging into Meditation and outdoor fun activities. I've heard that the blissful mountains in Gangtok are amazing. Try to plan a small holiday trip and clear your mind off. See! there are so many things to enjoy life.", ctl

def analyze_ocd(a_dict, b_dict, c_dict):
    final_dict = dictionary_generator(a_dict, b_dict, c_dict)
    generate_report(final_dict)
    ctl = "analysis_done"
    return "From what I have studied, you are showing mild symptoms of a condition known as Obsessive Compulsive Disorder. Since this condition can even lead to other conditions like anxiety and depression, I would suggest you to go see a doctor.\nApart from that, try consuming more proteins in your diet, start exercising and indulging in outdoor sports more.\nKeep your brain and body more busy and active and you'll be good to go. Also, don't be scared to go to a doctor. This is just a phase and not a disease.", ctl

def analyze_stress(a_dict, b_dict):
    final_dict = dictionary_generator_forstress(a_dict, b_dict)
    generate_report(final_dict)
    ctl = "analysis_done"
    return "From what I have studied, it looks like you are a bit stressed out. It may be due to the work you do all day. Take a chill pill and relax a bit. I've heard that mountains in the Gangtok are amazing to trek.\nIf you want to stay at home, then get more sleep, have healthy food and indulge into some hobbies for next few days. There is only one way to get yourself out of this, that is to relax your mind and body.\nPractice some Yoga and Meditation for recreation and listen to some soulful music.", ctl

def dictionary_generator_forstress(a_dict, b_dict):
    generated_dict = {**a_dict, **b_dict}
    return generated_dict

def dictionary_generator(a_dict, b_dict, c_dict):
    generated_dict = {**a_dict, **b_dict, **c_dict}
    return generated_dict

# print(analyze_anxiety({'restlessness'   : 1,
#                   'uneasiness'     : 0,
#                   'tension'        : 1}, {'relax'          : 1,
#                                     'energy'         : 1}, {'appetite'        : 0,
#                                                       'sleep'           : 0,
#                                                       'concentration'   : 0}))
