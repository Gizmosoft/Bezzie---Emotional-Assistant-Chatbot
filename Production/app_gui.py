from tkinter import *
import time
import tkinter.messagebox
from gtts import gTTS
from playsound import playsound
import os
import threading
from nltk_model import *
from conversation import *
from listen import *
from diagnosis import *
from report import *

window_size="800x600"
ctrl = "default"
class ChatInterface(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # sets default bg for top level windows
        self.tl_bg = "#EEEEEE"
        self.tl_bg2 = "#EEEEEE"
        self.tl_fg = "#000000"
        self.font = "Verdana 10"

        menu = Menu(self.master)
        self.master.config(menu=menu, bd=5)
# Menu bar

    # File
        file = Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file)
        file.add_command(label="Exit",command=self.chatexit)

        help_option = Menu(menu, tearoff=0)
        menu.add_cascade(label="Help", menu=help_option)
        #help_option.add_command(label="Features", command=self.features_msg)
        help_option.add_command(label="About Bezzie", command=self.msg)
        help_option.add_command(label="Developers", command=self.about)

        self.text_frame = Frame(self.master, bd=6)
        self.text_frame.pack(expand=True, fill=BOTH)

        # scrollbar for text box
        self.text_box_scrollbar = Scrollbar(self.text_frame, bd=0)
        self.text_box_scrollbar.pack(fill=Y, side=RIGHT)

        # contains messages
        self.text_box = Text(self.text_frame, yscrollcommand=self.text_box_scrollbar.set, state=DISABLED,
                             bd=1, padx=6, pady=6, spacing3=8, wrap=WORD, bg=None, font="Verdana 10", relief=GROOVE,
                             width=10, height=1)
        self.text_box.pack(expand=True, fill=BOTH)
        self.text_box_scrollbar.config(command=self.text_box.yview)

        # frame containing user entry field
        self.entry_frame = Frame(self.master, bd=1)
        self.entry_frame.pack(side=LEFT, fill=BOTH, expand=True)

        # entry field
        self.entry_field = Entry(self.entry_frame, bd=1, justify=LEFT)
        self.entry_field.pack(fill=X, padx=6, pady=6, ipady=3)
        # self.users_message = self.entry_field.get()

        # frame containing send button and emoji button
        self.send_button_frame = Frame(self.master, bd=0)
        self.send_button_frame.pack(fill=BOTH)

        # send button
        self.send_button = Button(self.send_button_frame, text="SEND", width=5, relief=GROOVE, bg='#483D8B',
                                  bd=1, command=lambda: self.send_message_insert(None), activebackground="#483D8B",
                                  activeforeground="#ffffff", fg="#ffffff")
        self.send_button.pack(side=LEFT, ipady=8)
        self.master.bind("<Return>", self.send_message_insert)

        self.last_sent_label(date="No messages sent.")

    def font_change_default(self):
        self.text_box.config(font="Verdana")
        self.entry_field.config(font="Verdana")
        self.font = "Verdana"

    def color_theme_default(self):
        self.master.config(bg="#263b54")
        self.text_frame.config(bg="#263b54")
        self.text_box.config(bg="#1c2e44", fg="#FFFFFF")
        self.entry_frame.config(bg="#263b54")
        self.entry_field.config(bg="#1c2e44", fg="#FFFFFF", insertbackground="#FFFFFF")
        self.send_button_frame.config(bg="#263b54")
        self.send_button.config(bg="#1c2e44", fg="#FFFFFF", activebackground="#1c2e44", activeforeground="#FFFFFF")
        #self.emoji_button.config(bg="#1c2e44", fg="#FFFFFF", activebackground="#1c2e44", activeforeground="#FFFFFF")
        self.sent_label.config(bg="#263b54", fg="#FFFFFF")

        self.tl_bg = "#1c2e44"
        self.tl_bg2 = "#263b54"
        self.tl_fg = "#FFFFFF"

    def last_sent_label(self, date):

        try:
            self.sent_label.destroy()
        except AttributeError:
            pass

        self.sent_label = Label(self.entry_frame, font="Verdana 7", text=date, bg=self.tl_bg2, fg=self.tl_fg)
        self.sent_label.pack(side=LEFT, fill=X, padx=3)

    def clear_chat(self):
        self.text_box.config(state=NORMAL)
        self.last_sent_label(date="No messages sent.")
        self.text_box.delete(1.0, END)
        self.text_box.delete(1.0, END)
        self.text_box.config(state=DISABLED)

    def chatexit(self):
        exit()

    def msg(self):
        tkinter.messagebox.showinfo("Bezzie, the Chatbot v0.1 - alpha build",'Bezzie is a chatbot made with love for you!\nIf you find yourself struggling to share things about your life then Bezzie is for you. She will be the best friend for all your problems.')

    def about(self):
        tkinter.messagebox.showinfo("Bezzie, the Chatbot - Team","Developed at Bangalore Institute of Technology, Bengaluru.\n\nDevelopers:\nKartikey V Hebbar, Amritesh Anand, Hrithik Jain, Rajat Sahay.\n")

    def speak(self, sentence):
        v = gTTS(text=sentence,lang="en",slow=False)
        filename = "test.mp3"
        v.save(filename)
        playsound(filename)
        if os.path.exists(filename):
            os.remove(filename)

    def display_speak(self, pr, ob):
        #DISPLAY AND SPEAK - Bezzie
        self.text_box.configure(state=NORMAL)
        self.text_box.insert(END, pr)
        self.text_box.configure(state=DISABLED)
        self.text_box.see(END)
        self.last_sent_label(str(time.strftime( "Last message sent: " + '%B %d, %Y' + ' at ' + '%I:%M %p')))
        self.entry_field.delete(0,END)
        time.sleep(0)
        t2 = threading.Thread(target=self.speak, args=(ob,))
        t2.start()

    def send_message_insert(self, message):
        global ctrl
        user_input = self.entry_field.get()
        pr1 = "User : " + user_input + "\n"
        self.text_box.configure(state=NORMAL)
        self.text_box.insert(END, pr1)
        self.text_box.configure(state=DISABLED)
        self.text_box.see(END)

        if(ctrl=="default"):
            ob=welcome()
            ctrl = ob[1]
            ob=ob[0]
            pr="Bezzie : " + ob + "\n"
            a.display_speak(pr, ob)
        elif(ctrl=="welcome"):
            if(user_input!="bye"):
                ob=bezzie_chat1(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="nltk1"):
            if(user_input!="bye"):
                ob=bezzie_chat2(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="nltk2"):
            if(user_input!="bye"):
                ob=bezzie_chat3(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="nltk3"):
            if(user_input!="bye"):
                ob=bezzie_chat4(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
                time.sleep(3)
                if os.path.exists("test.mp3"):
                    os.remove("test.mp3")
                ob=chatbot_controller()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="chatbot"):
            if(user_input!="bye"):
                ob=how_do_you_feel(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="permission"):
            if(user_input!="bye"):
                ob=listening1(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="listening1"):
            if(user_input!="bye"):
                ob=listening2(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="listening2"):
            if(user_input!="bye"):
                ob=listening3(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="listening3"):
            if(user_input!="bye"):
                ob=anything_else(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="confirm"):
            if(user_input!="bye"):
                ob=confirmation(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="diagnose"):
            if(user_input!="bye"):
                ob=restlessness(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="restless"):
            if(user_input!="bye"):
                ob=uneasiness(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="uneasy"):
            if(user_input!="bye"):
                ob=tension(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="tension"):
            if(user_input!="bye"):
                ob=diagnosis_stage1(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="diagnosis_stage1"):
            if(user_input!="bye"):
                ob=guilt(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="guilt"):
            if(user_input!="bye"):
                ob=diagnosis_stage2(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="diagnosis_stage2"):
            if(user_input!="bye"):
                ob=repetitive_thoughts(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="repeats"):
            if(user_input!="bye"):
                ob=diagnosis_stage3(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="diagnosis_stage3"):
            if(user_input!="bye"):
                ob=energy(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="energy"):
            if(user_input!="bye"):
                ob=diagnosis_stage4(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="anxiety_detected"):
            if(user_input!="bye"):
                ob=anxietyGen1(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="anxietyGen1"):
            if(user_input!="bye"):
                ob=anxietyGen2(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="anxietyGen2"):
            if(user_input!="bye"):
                ob=anxietyGen3(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="anxietyGen3"):
            if(user_input!="bye"):
                ob=anxietyGen4(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
                time.sleep(12)
                if os.path.exists("test.mp3"):
                    os.remove("test.mp3")
                ob=diagnosed_anxiety_analysis()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="depression_detected"):
            if(user_input!="bye"):
                ob=depressionGen1(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="depressionGen1"):
            if(user_input!="bye"):
                ob=depressionGen2(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="depressionGen2"):
            if(user_input!="bye"):
                ob=depressionGen3(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="depressionGen3"):
            if(user_input!="bye"):
                ob=depressionGen4(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="depressionGen4"):
            if(user_input!="bye"):
                ob=depressionGen5(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="depressionGen5"):
            if(user_input!="bye"):
                ob=depressionGen6(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
                time.sleep(12)
                if os.path.exists("test.mp3"):
                    os.remove("test.mp3")
                ob=diagnosed_depression_analysis()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="ocd_detected"):
            if(user_input!="bye"):
                ob=ocdGen1(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="ocdGen1"):
            if(user_input!="bye"):
                ob=ocdGen2(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="ocdGen2"):
            if(user_input!="bye"):
                ob=ocdGen3(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="ocdGen3"):
            if(user_input!="bye"):
                ob=ocdGen4(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
                time.sleep(12)
                if os.path.exists("test.mp3"):
                    os.remove("test.mp3")
                ob=diagnosed_ocd_analysis()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="stress_detected"):
            if(user_input!="bye"):
                ob=stressGen1(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="stressGen1"):
            if(user_input!="bye"):
                ob=stressGen2(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="stressGen2"):
            if(user_input!="bye"):
                ob=stressGen3(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="stressGen3"):
            if(user_input!="bye"):
                ob=stressGen4(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="stressGen4"):
            if(user_input!="bye"):
                ob=stressGen5(user_input)
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
                # time.sleep(4)
                if os.path.exists("test.mp3"):
                    os.remove("test.mp3")
                ob=diagnosed_stress_analysis()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
            else:
                ob=goodbye()
                ctrl = ob[1]
                ob=ob[0]
                pr="Bezzie : " + ob + "\n"
                a.display_speak(pr, ob)
        elif(ctrl=="analysis_done"):
            ob = "I'll be here around if you need me. Just talk to me whenever you feel like. Bye!"
            ctrl = "default"
            pr="Bezzie : " + ob + "\n"
            a.display_speak(pr, ob)
        else:
            ob="Oops! I was lost in daydreaming. Sorry. Let's start again"
            ctrl="welcome"
            pr="Bezzie : " + ob + "\n"
            a.display_speak(pr, ob)


    # Default font and color theme
    def default_format(self):
        self.font_change_default()
        self.color_theme_default()


root=Tk()

a = ChatInterface(root)
root.geometry(window_size)
root.title("Bezzie, the Chatbot")
root.iconbitmap('resources/bezzie.ico')
root.mainloop()
