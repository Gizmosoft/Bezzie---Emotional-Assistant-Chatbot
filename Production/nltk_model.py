from __future__ import print_function
from nltk.chat.util import Chat, reflections

control = ""
pairs = (
    (r'quit',
     ( "Thank you. It was good talking to you.",
       "Good-bye.")),

    (r'Who (are|is)(.*)',
     ( "My name is Bezzie.",
       "I'm Bezzie, the chatbot.")),

    (r'(.*)(Nice|Same|wonderful|wow|great|good|awesome)(.*)',
     ( "Cheers!",
       "Cool.")),

    (r'How (.*) know (.*)',
     ( "Because I'm your friend.",
       "Because I care for you.")),

    (r'What is your name(.*)',
     ( "My name is Bezzie.",
       "I'm Bezzie.")),

    (r'(.*)What do you (.*)',
     ( "I help people by becoming their best friend.",
       "I like to talk about life. Your life.",
       "I like making friends and helping them out.")),

    (r'How are you(.*)',
     ( "I am fine. Thank You.",
       "I am fine.",
       "Fine. Thank You.")),

    (r'Will (.*) help me',
     ( "Of course. Why not?",
       "For sure. That's why I'm here.",
       "No fear when Bezzie is here!")),

    (r'Will (.*) friend',
     ( "Of course. Why not?",
       "For sure. That's why I'm here.")),

    (r'Hi(.*)',
     ( "Hi!",
       "Hello.",
       "Hi. Great to meet you.")),

    (r'Hey(.*)',
     ( "Hi!",
       "Hello.",
       "Hi. Great to meet you.")),

    (r'My name is (.*)',
     ( "Hi %1.",
       "Hello %1.",
       "Hi %1. Nice to meet you.")),

    (r'(.*) (I\'m|I am) (.*)',
     ( "I know you, %2",
       "Of course I know you")),

    (r'You tell me(.*)',
     ( "I am more of a listener.",
       "I love to listen to stories. Tell me yours.")),

    (r'Hello(.*)',
     ( "Hi.",
       "Hello")),

    (r'Yes',
     ( "You seem certain.",
       "Alright")),

    (r'(.*)Cool',
     ( "Yes I am.",
       "Yep!")),

    (r'(.*) (happy|cheerful|glad|good)',
     ( "That's good.",
       "That's awesome!")),

    (r'(.*) help me',
     ( "Just tell me whatever is in your mind. I'll tell you the rest.",
       "If something is wrong, just let me know. I'll try to help.")),

    (r'Who (created|developed|made) you',
     ( "Some amazing minds! Check the developers tag in the Menu to know more.",
       "Some brilliant minds in Bangalore Institute of Technology! Check the developers tag in the Menu to know more.")),

    (r'(.*)(oh|okay|ok|i see|good)',
     ( "Yes.",
       "Yeah.")),

    (r'what',
     ( "Nothing here",
       "Nothing much",
       "All good here.")),

    (r'(.*)(yeah|ya|yes|yep)',
     ( "Yes",
       "Ya"))
)

bezzie = Chat(pairs, reflections)

def bezzie_chat1(sentence):
    # bezzie.converse()
    ## PRINT TO SEE THE OUTPUT ON TERMINAL
    # print(bezzie.respond(sentence))
    control = "nltk1"
    return bezzie.respond(sentence), control

def bezzie_chat2(sentence):
    control = "nltk2"
    return bezzie.respond(sentence), control

def bezzie_chat3(sentence):
    control = "nltk3"
    return bezzie.respond(sentence), control

def bezzie_chat4(sentence):
    control = "nltk4"
    return bezzie.respond(sentence), control

#call with a str parameter
# bezzie_chat(sentence)
