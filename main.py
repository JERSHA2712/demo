import speech_recognition as sr
import pyttsx3
import os
from ecapture import ecapture
import datetime
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.clock import Clock




#setting up voice
tasha=pyttsx3.init()
voices= tasha.getProperty('voices')
tasha.setProperty('voice', voices[1].id)  #female voice
tasha.setProperty('rate', 175)            #words per minute

#setting up recognizer
listener= sr.Recognizer()


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
        return "Unable to recognize. Something must be wrong :("

Builder.load_file('output_label.kv')

class MyLayout(Widget):
    def press(self):
        task = listen()
        task = task.lower()

        if 'open' in task:
            if 'google chrome' in task:
                say("Opening Google chrome")
                self.ids.outputLabel.text = "Opening Google Chrome..."
                path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"
                os.startfile(path)

            elif 'microsoft edge' in task:
                say("Opening Microsoft Edge")
                self.ids.outputLabel.text = "Opening Microsoft Edge..."
                path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.lnk"
                os.startfile(path)

            elif 'word' in task:
                say("Opening Microsoft Word")
                self.ids.outputLabel.text = "Opening Microsoft Word..."
                path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk"
                os.startfile(path)

            elif 'powerpoint' in task:
                say("Opening Microsoft PowerPoint")
                self.ids.outputLabel.text = "Opening Microsoft PowerPoint..."
                path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk"
                os.startfile(path)

            elif 'excel' in task:
                say("Opening Microsoft Excel")
                self.ids.outputLabel.text = "Opening Microsoft Excel..."
                path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk"
                os.startfile(path)

            elif 'browser' in task:
                say("Opening default Browser")
                self.ids.outputLabel.text = "Opening default Browser..."
                path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"
                os.startfile(path)

            elif 'code blocks' in task:
                say("Opening CodeBlocks")
                self.ids.outputLabel.text = "Opening CodeBlocks..."
                path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\CodeBlocks\CodeBlocks.lnk"
                os.startfile(path)

            elif 'photo shop' in task:
                say("Opening Adobe Photoshop 2020")
                self.ids.outputLabel.text = "Opening Adobe Photoshop 2020..."
                path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Adobe Photoshop 2020.lnk"
                os.startfile(path)

            elif 'pdf reader' in task:
                say("Opening Adobe Reader 9")
                self.ids.outputLabel.text = "Opening Adobe Reader 9..."
                path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Adobe Reader 9.lnk"
                os.startfile(path)

        elif 'camera' or 'take picture' in task:
            say("Say cheese!")
            self.ids.outputLabel.text = "Photo taken"
            ecapture.capture(0, "photo", "img.jpg")

        elif 'hello' in task:
            say("Hello human")
            self.ids.outputLabel.text = "Hello human!"

        elif 'how are you' in task:
            say('I am fine, thank you! How are you?')
            self.ids.outputLabel.text = "I am fine, thank you! How are you?"

        elif 'fine' or 'good':
            say("It's good to know that you are fine")
            self.ids.outputLabel.text = "It's good to know that you are fine"

        else:
            say("Sorry, Didn't get you quite right!")
            self.ids.outputLabel.text = "Sorry, Didn't get you quite right! Try speaking precisely"


class MyApp(App):
    def build(self):
        return MyLayout()


MyApp().run()
































