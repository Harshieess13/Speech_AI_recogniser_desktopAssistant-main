import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
from tkinter import *


def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening')
        r.pause_threshold = 0.7
        audio = r.listen(source)

        try:
            print("Recognizing")

            # for command in indian english use 'hi-In'
            Query = r.recognize_google(audio, language='en-in')
            print("the command is '{}'".format(Query))

        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"

        return Query


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # [0]=male & [1]=female voice

    engine.setProperty('voice', voices[1].id)

    engine.say(audio)

    engine.runAndWait()


def tellDay():
    day = datetime.datetime.today().weekday() + 1

    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)


def tellTime():
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    minutes = time[14:16]
    speak("Sir, the time is" + hour + "Hours and" + minutes + "Minutes")


def hello():
    speak("Hello sir, What can I do for you")


def Take_query():
    hello()

    while True:

        query = takeCommand().lower()
        if "open youtube" in query:
            speak("Opening youtube ")

            webbrowser.open("www.youtube.com")
            continue

        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue

        elif "which day it is" in query:
            tellDay()
            continue

        elif "what time is it now" in query:
            tellTime()
            continue

        elif "bye" in query:
            speak("Thank You and Good Bye")
            exit()

        elif "from wikipedia" in query:

            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")

            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)

        elif "Who are you" in query:
            speak("I am IVA, Your desktop Assistant")


def main_screen():

    screen = Tk()
    screen.title('Intelligent Virtual Assistant')
    screen.geometry("500x500")
    screen.resizable(width=False, height=False)

    microphone_photo = PhotoImage(file="./lib/gifloader.gif")
    microphone_button = Button(image=microphone_photo, command=takeCommand())
    # microphone_button = Button(image=microphone_photo)
    microphone_button.pack(pady=0)

    screen.mainloop()


if __name__ == '__main__':
    main_screen()
    # Take_query()
