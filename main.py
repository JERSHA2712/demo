import speech_recognition as sr
import pyttsx3
import os
from ecapture import ecapture
import datetime
import subprocess
import ctypes
import requests
import webbrowser
import winshell


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

        if 'hello' in task:
            say("Hello human")
            self.ids.outputLabel.text = "Hello human!"

        elif 'how are you' in task:
            say('I am fine, thank you! How are you?')
            self.ids.outputLabel.text = "I am fine, thank you! How are you?"

        elif 'open' in task:
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

            elif 'photoshop' in task:
                say("Opening Adobe Photoshop 2020")
                self.ids.outputLabel.text = "Opening Adobe Photoshop 2020..."
                path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Adobe Photoshop 2020.lnk"
                os.startfile(path)

            elif 'pdf reader' in task:
                say("Opening Adobe Reader 9")
                self.ids.outputLabel.text = "Opening Adobe Reader 9..."
                path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Adobe Reader 9.lnk"
                os.startfile(path)

            elif "wikipedia" in task:
                say("Opening Wikipedia")
                self.ids.outputLabel.text = "Opening Wikipedia..."
                webbrowser.open("https://en.wikipedia.org/wiki/Main_Page")

            elif "nucleus" in task:
                say("Opening nucleus")
                self.ids.outputLabel.text = "Opening Nucleus..."
                webbrowser.open("https://nucleus.amcspsgtech.in/login")

            elif "gmail" in task:
                say("Opening Gmail")
                self.ids.outputLabel.text = "Opening Gmail..."
                webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")

            elif "whatsapp" in task:
                say("Opening WhatsApp")
                self.ids.outputLabel.text = "Opening WhatsApp..."
                webbrowser.open("https://web.whatsapp.com/")

            elif "prime video" in task:
                say("Opening Amazon primevideo")
                self.ids.outputLabel.text = "Opening Amazon primevideo..."
                webbrowser.open("https://www.primevideo.com/")

            elif "youtube" in task:
                say("Opening YouTube")
                self.ids.outputLabel.text = "Opening YouTube..."
                webbrowser.open("https://www.youtube.com/")

            elif "stack overflow" in task:
                say("Opening stackoverflow")
                self.ids.outputLabel.text = "Opening stackoverflow..."
                webbrowser.open("https://stackoverflow.com/")

            elif "google" in task:
                say("Opening Google")
                self.ids.outputLabel.text = "Opening Google..."
                webbrowser.open("https://www.google.com/")

            else:
                pass

        elif 'play music' in task or "play song" in task:
            say("Get ready for some grooving!")
            mudir = r"C:\Users\Tamjid L\Music"
            songs = os.listdir(mudir)
            self.ids.outputLabel.text = "Now playing  " + songs[0] + "..."
            random = os.startfile(os.path.join(mudir, songs[0]))

        elif 'time' in task:
            time = str(datetime.datetime.now())
            hour = time[11:13]
            min = time[14:16]
            self.ids.outputLabel.text = hour + ":" + min

            say("The time is " + hour + " " + min)

        elif ' day' in task:
            if 'today' in task:
                day = datetime.datetime.today().weekday() + 1
                if day == 1:
                    today = 'Monday'
                elif day == 2:
                    today = 'Tuesday'
                elif day == 3:
                    today = 'Wednesday'
                elif day == 4:
                    today = 'Thursday'
                elif day == 5:
                    today = 'Friday'
                elif day == 6:
                    today = 'Saturday'
                else:
                    today = 'Sunday'
                self.ids.outputLabel.text = 'Today is ' + today
                say("It is " + today + " today.")

            elif 'tomorrow' in task:
                day = datetime.datetime.today().weekday() + 2
                day = day % 7
                if day == 1:
                    tomorrow = 'Monday'
                elif day == 2:
                    tomorrow = 'Tuesday'
                elif day == 3:
                    tomorrow = 'Wednesday'
                elif day == 4:
                    tomorrow = 'Thursday'
                elif day == 5:
                    tomorrow = 'Friday'
                elif day == 6:
                    tomorrow = 'Saturday'
                else:
                    tomorrow = 'Sunday'
                self.ids.outputLabel.text = 'Tomorrow is ' + tomorrow
                say("It is " + tomorrow + " tomorrow.")
            else:
                day = datetime.datetime.today().weekday() + 1
                if day == 1:
                    today = 'Monday'
                elif day == 2:
                    today = 'Tuesday'
                elif day == 3:
                    today = 'Wednesday'
                elif day == 4:
                    today = 'Thursday'
                elif day == 5:
                    today = 'Friday'
                elif day == 6:
                    today = 'Saturday'
                else:
                    today = 'Sunday'
                self.ids.outputLabel.text = 'Today is ' + today
                say("It is " + today + " today.")

        elif 'date' in task:
            date = datetime.datetime.now().strftime("%d")
            month = datetime.datetime.now().strftime('%B')
            self.ids.outputLabel.text = 'Today is ' + month + " " + date
            say("It is, " + month + " " + date)

        elif 'lock window' in task:
            self.ids.outputLabel.text = "Locking the device"
            say("Locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown' in task:
            self.ids.outputLabel.text = "Shutting down"
            say("Shutting down, miss you!")
            subprocess.call('shutdown / p / f')

        elif 'restart' in task:
            self.ids.outputLabel.text = "Restarting"
            say("Restarting")
            subprocess.call(["shutdown", "/r"])

        elif 'empty recycle bin' in task:
            say("Emptying recycle bin")
            winshell.recycle_bin().empty(confirm=True, show_progress=False, sound=True)
            self.ids.outputLabel.text = "Recycle bin emptied..."

        elif 'camera' in task or 'take picture' in task:
            say("Say cheese!")
            self.ids.outputLabel.text = "Photo taken"
            ecapture.capture(0, "photo", "img.jpg")

        elif 'fine' in task or 'good' in task:
            say("It's good to know that you are fine")
            self.ids.outputLabel.text = "It's good to know that you are fine"

        elif "weather" in task:
            say("Fetching weather report")
            api_key = "774e65031b515e2c113ae44e18559e75"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            complete_url = base_url + "q=" + "Pondicherry" + "&appid=" + api_key
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                self.ids.outputLabel.text ="Temperature (in kelvin unit)= " + str(
                    current_temperature) + "\nAtmospheric pressure (in hPa unit)= " + str(
                    current_pressure) + "\nHumidity (in percentage)= " + str(
                    current_humidity) + "\n\nDescription= " + str(weather_description)
            else:
                say(" Can't fetch at the moment!")

        else:
            say("Sorry, Didn't get you quite right!")
            self.ids.outputLabel.text = "Sorry, Didn't get you quite right! Try speaking precisely"


class MyApp(App):
    def build(self):
        return MyLayout()


MyApp().run()































