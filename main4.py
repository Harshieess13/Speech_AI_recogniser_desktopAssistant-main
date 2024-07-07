import pyttsx3
import AppOpener
import tkinter
import os
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import subprocess
import time


# this method is for taking the commands
# and recognizing the command from the
# speech_Recognition module we will use
# the recognizer method for recognizing

def takeCommand():
    r = sr.Recognizer()

    # from the speech_Recognition module
    # we will use the Microphone module
    # for listening the command
    with sr.Microphone() as source:
        print('Listening')

        # seconds of non-speaking audio before
        # a phrase is considered complete
        r.pause_threshold = 0.7
        audio = r.listen(source)

        # Now we will be using the try and catch
        # method so that if sound is recognized
        # it is good else we will have exception
        # handling
        try:
            print("Recognizing")

            # for Listening the command in indian
            # english we can also use 'hi-In'
            # for hindi recognizing
            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)

        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"

        return Query


def speak(audio):
    engine = pyttsx3.init()
    # getter method(gets the current value
    # of engine property)
    voices = engine.getProperty('voices')

    # setter method .[0]=male voice and
    # [1]=female voice in set Property.
    engine.setProperty('voice', voices[0].id)

    # Method for the speaking of the assistant
    engine.say(audio)

    # Blocks while processing all the currently
    # queued commands
    engine.runAndWait()


def tellDay():
    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1

    # this line tells us about the number that will help us in telling the day

    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)


def tellTime():
    # This method will give the time
    time = str(datetime.datetime.now())

    # the time will be displayed like
    # this "2020-06-05 17:50:14.582630"
    # and then after slicing we can get time
    print(time)
    hour = time[11:13]
    minutes = time[14:16]
    speak("The time is sir" + hour + "Hours and" + minutes + "Minutes")


def hello():
    # This function is for when the assistant
    # is called it will say hello and then
    # take query
    speak("Hello sir, What can I do for you")


def Take_query():
    # calling the Hello function for
    # making it more interactive
    hello()

    # This loop is infinite as it will take
    # our queries continuously until and unless
    # we do not say bye to exit or terminate
    # the program
    while True:

        # taking the query and making it into
        # lower case so that most of the times query matches, and we get the perfect output

        query = takeCommand().lower()
        if "open youtube" in query:
            speak("Opening youtube ")

            # in the open method we just to give the link of the website, and it automatically opens
            # it in your default browser
            webbrowser.open("www.youtube.com")
            continue

        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue

        elif "open song" in query:
            speak("Opening Song ")
            from playsound import playsound
            playsound('C:\\Users\\mitta\\OneDrive\\Desktop\\Soniyo.mp3')
            continue

        elif "songs" in query:
            speak("Opening Song")
            from playsound import playsound
            playsound("C:\\Users\\mitta\\OneDrive\\Desktop\\Soniyo2.mp3")
            continue

        elif "open ms" in query:
            speak("Opening Edge")
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.lnk")
            continue

        elif "open spotify" in query:
            speak("Opening Spotify ")
            webbrowser.open("https://open.spotify.com")
            continue

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "turn off system" in query:
            speak("Hold a sec your system is going to shut down")
            os.system("shutdown /s /t 1")


        elif "open hackerrank" in query:
            speak("Opening Hackerrank ")
            webbrowser.open("www.hackerrank.com")
            continue

        elif "sleep" in query:
            speak("Going to Sleep Mode ")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            
        elif "open linkedin" in query:
            speak("Opening LinkedIn ")
            webbrowser.open("https://in.linkedin.com")
            continue


        elif "open wikipedia" in query:
            speak("Opening Wikipedia ")
            webbrowser.open("www.wikipedia.com")
            continue

        elif "open whatsapp" in query:
            speak("Opening Whatsapp ")
            from AppOpener import run
            run("Whatsapp")
            continue

        elif "open media player" in query:
            speak("Opening Media Player ")
            from AppOpener import run
            run("Media Player")
            continue

        elif "open mail" in query:
            speak("Opening Mail")
            from AppOpener import run
            run("Mail")
            continue

        elif "open office" in query:
            speak("Opening Office ")
            from AppOpener import run
            run("Office")
            continue

        elif "open office" in query:
            speak("Opening Office ")
            from AppOpener import run
            run("Office")
            continue

        elif "launch Word" in query:
            speak("Opening Word")
            from AppOpener import run
            run("Word")
            continue

        elif "launch PowerPoint" in query:
            speak("Opening Powerpoint")
            from AppOpener import run
            run("PowerPoint")
            continue

        elif "launch Excel" in query:
            speak("Opening Excel")
            from AppOpener import run
            run("Excel")
            continue

        

        elif "open messenger" in query:
            speak("Opening Messenger")
            from AppOpener import run
            run("Messenger")
            continue

        elif "launch spotify" in query:
            speak("Opening Spotify ")
            from AppOpener import run
            run("Spotify")
            continue

        elif "open settings" in query:
            speak("Opening Settings ")
            from AppOpener import run
            run("Settings")
            continue

       
        elif "which day it is" in query:
            tellDay()
            continue

        elif "tell me the time" in query:
            tellTime()
            continue

        # this will exit and terminate the program

        elif "bye" in query:
            speak("Thank You and Good Bye")
            exit()

        elif "from wikipedia" in query:

            # if anyone wants to have information from wikipedia
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")

            # it will give the summary of 4 lines from
            # wikipedia we can increase and decrease
            # it also.
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)

        elif "tell me your name" in query:
            speak("I am IVA, Your desktop Assistant")


if __name__ == '__main__':
    # main method for executing
    # the functions
    Take_query()
