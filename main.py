import speech_recognition as sr
import pyttsx3
import datetime
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder

#setting up voice
tasha=pyttsx3.init()
voices= tasha.getProperty('voices')
tasha.setProperty('voice', voices[1].id)  #female voice
tasha.setProperty('rate', 175)            #wordsperminute

#setting up recognizer
listener= sr.Recognizer()


class MyLabelApp(App):
    def build(self):



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
    label = MyLabelApp()
    label.run()
    tasha.say(info)
    tasha.runAndWait()

def listen():
    try:
        with sr.Microphone() as ears:
            print("Listening...")
            audio = listener.listen(ears)
            data = listener.recognize_google(audio)
            print(data)
            data= data.lower()
    except:
            print("There must be something wrong...")

greet()

































