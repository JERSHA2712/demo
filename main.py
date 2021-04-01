import speech_recognition as sr
import pyttsx3
import datetime
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder



#setting up voice
tasha=pyttsx3.init()
voices= tasha.getProperty('voices')
tasha.setProperty('voice', voices[1].id)  #female voice
tasha.setProperty('rate', 175)            #words per minute

#setting up recognizer
listener= sr.Recognizer()




def greet():

    time= int(datetime.datetime.now().hour)
    if time>=0 and time<12:
        say("Good morning!")
    elif time>=12 and time<18:
        say("Good afternoon!")
    else:
        say("Good evening")
    say("I am your virtual voice assistant, Tasha 2 point 0!")

def say(info):
    tasha.say(info)
    tasha.runAndWait()

def listen():
    try:
        with sr.Microphone() as ears:
            audio = listener.listen(ears)
            data = listener.recognize_google(audio)
            return data
    except:
        return "Something must be wrong"

Builder.load_file('output_label.kv')

class MyLayout(Widget):
    def press(self):
        output = listen()
        self.ids.outputLabel.text = output

class MyApp(App):
    def build(self):
        return MyLayout()

MyApp().run()

































