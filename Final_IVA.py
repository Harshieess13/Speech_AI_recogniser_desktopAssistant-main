import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import time
import sounddevice as sd
import os
import wavio as wv
from googletrans import Translator
from AppOpener import run

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
            # hindi we can also use 'hi-In'
            Query = r.recognize_google(audio, language='en-in')
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
    engine.setProperty('voice', voices[1].id)

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
    # this "YYYY-MM-DD hh:mm:ss"
    # and then after slicing we can get time
    print(time)
    hour = time[11:13]
    minutes = time[14:16]
    speak("The time is sir" + hour + "Hours and" + minutes + "Minutes")


def hello():
    # This function is for when the assistant
    # is called it will say hello and then
    # take query
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        speak("Good Morning Sir! What can I do for you")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon Sir! What can I do for you")  
  
    else:
        speak("Good Evening Sir! What can I do for you")

def record():
    #When this function is called it will
    #record the audio input provided 
    #in the form of audio
    freq = 44100
    duration = 5
    recording = sd.rec(int(duration * freq),samplerate=freq, channels=2)
    sd.wait()
    wv.write("D:\VIDIT\Coding\Python\Projects\\AI Assistant\main\\recording0.wav", recording, freq, sampwidth=2)

def note():
    #When this function is called it will
    #record the audio input provided 
    #in the form of text
    speak("What should i write, sir")
    note = takeCommand()
    print(note)
    file1 = open("D:\VIDIT\Coding\Python\Projects\\AI Assistant\main\\newfile.txt", "a")
    speak("Sir, Should i include date and time")
    write_file= takeCommand()
    if 'yes' in write_file or 'sure' in write_file:
        strTime = datetime.datetime.now().strftime("% H:% M:% S") ##########CHECK HERE###############
        file1.write(strTime)
        file1.write(" :- ")
        file1.write(note)
    elif "no" in write_file:
        file1.write(note)
    file1.close()
    file2=open("D:\VIDIT\Coding\Python\Projects\\AI Assistant\main\\newfile.txt","r")
    speak("Do you want me to read the contents of your file")
    read_file=takeCommand()
    if 'yes' in read_file:
        a=file2.read()
        speak(a)
    else:
        pass
    file2.close()

def ShowNotes():
    #When this function is called it will
    #show the notes taken 
    time.sleep(2)
    print("..")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("....")
    time.sleep(1)
    os.startfile("D:\VIDIT\Coding\Python\Projects\\AI Assistant\main\\newfile.txt")

def translate():
    #This code will tranlate the given input to
    #English Language
    trans=takeCommand()
    translator = Translator()
    translation = translator.translate(trans, dest='en')
    speak1=translation.text
    speak(speak1)

def Take_query():
    # This loop is infinite as it will take
    # our queries continuously until and unless
    # we do not say bye to exit or terminate
    # the program

    
    while True:
        # taking the query and making it into
        # lower case so that most of the times query matches, and we get the perfect output
        query1 = takeCommand().lower()
        if "ok computer" in query1:
            hello()
            query=takeCommand().lower()

            # in the open method we just to give the link of the website, and it automatically opens
            # it in your default browser
            if "open youtube" in query:
                speak("Opening youtube ")
                webbrowser.open("www.youtube.com")
            elif "open google" in query:
                speak("Opening Google ")
                webbrowser.open("www.google.com")
            elif "which day it is" in query:
                tellDay()
            elif "tell me the time" in query:
                tellTime()

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

            #Basic converstaion with the Assistant
            elif "tell me your name" in query:
                speak("I am IVA, Your desktop Assistant")

            elif 'how are you' in query:
                speak("I am fine, Thank you")
                speak("How are you, Sir")
 
            elif 'fine' in query or "good" in query:
                speak("It's good to know that your fine")

            elif "translate" in query:
                speak("What sentence do you want to translate")
                translate()

            elif "launch " in query:
                #This query is used to launch applications
                speak("Opening application")
                query = query.replace("launch", "")
                query2=query.strip()
                run(query2)

            elif "record" in query:
               speak("Recording")
               record()
#
            elif "write a note" in query:
                speak("Taking note")
                note()
#
            elif "show my notes" in query:
                speak("Showing your notes")
                ShowNotes()
         
            else:
                #If any query is unavailable in the existing queries
                #then this function searches on google for the query
                a=query.split(" ")
                c="+".join(a)
                speak("Searching for your query")
                webbrowser.open("https://www.google.com/search?q="+c)
        
        # this will exit and terminate the program        
        elif "bye" in query1:
                speak("Thank You and Good Bye")
                exit()    

                

if __name__ == '__main__':
    # main method for executing
    # the functions
    Take_query()