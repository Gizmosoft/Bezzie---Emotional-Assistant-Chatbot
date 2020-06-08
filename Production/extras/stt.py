import speech_recognition as sr

recognise = sr.Recognizer()

def configurer():
    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...")
        # listen for 5 seconds and create the ambient noise energy level
        recognise.adjust_for_ambient_noise(source, duration=5)
        print("Start Speaking.....")
    return listener()

def listener():
    with sr.Microphone() as source:
        audio = recognise.listen(source)

    try:
        text = format(recognise.recognize_google(audio))
        text = text.replace("busy", "Bezzie")
        return text, 200
        # print("You said : {}".format(recognise.recognize_google(audio)))
       # print("Module thinks you said '" + recognise.recognize_google(audio) + "'")
    except sr.UnknownValueError:
        return "Sorry, I didn't get you there. Can you please repeat?", 404
    except sr.RequestError as e:
        return "Sorry, I could not understant you", 404

## PROCEDURE TO GET ONLY TEXT FROM RETURNED VALUE
print('', listener()[0])
