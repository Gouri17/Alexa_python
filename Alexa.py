import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import tkinter as tk
from tkinter import *

engine = pyttsx3.init('sapi5') #take a inbuilt voice
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!!")
        T.insert(INSERT,"Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Aftenoon")
        T.insert(INSERT,"Good AfterNoon")
    else:
        speak("Good Evening!!")
        T.insert(INSERT,"Good Evening")

    speak("i am alexa please tellme how may i help you")
    T.insert(INSERT,"\ni am alexa please tellme how may i help you")

def takeCommand():  #it takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        T.insert(INSERT,"Listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognize...")
        T.insert(INSERT,"Recongnize")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:",query,"\n")
        T.insert(Insert,query)

    except:
        print("Say that again please...")
        return "None"
    return query



if __name__ == "__main__":
    r = tk.Tk()
    r.title("textbox")
    r.geometry('600x400')
    #r.minsize(600,400)
    
    T = Text(r, height=22, width=70,bd=7)
    T.pack()
    T.place(x=100,y=100)
    wishMe()
    r.mainloop()
    while True:
        query= takeCommand().lower() 


         # Logic for executing tasks based on query
        if 'tell me about' in query or 'what is' in query or 'search for' in query:
            speak("Searching for your question...")
            if query=="tell me about":
                query = query.replace("tell me about","")
            if query=="what is":
                query = query.replace("what is","")
            if query=="search for":
                query = query.replace("search for","")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia")
            print(results)
            T.insert(INSERT,results)
            speak(results)
            T.insert(INSERT,results)

        if 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        
        if 'open google' in query:
            webbrowser.open("www.google.com")

        if 'play music' in query:
            music_dir = 'F:\music\hindi song'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        if 'open images' in query:
            photo_dir = 'F:\GPS\CM Teachers Day Pic'
            photo=os.listdir(photo_dir)
            os.startfile(os.path.join(photo_dir, photo[0]))

        if 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is{strTime}")

        if 'open vs code' in query:
            codepath="C:\\Users\\Gouri\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        if 'open wordpad' in query:
            codepath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013"
            os.startfile(codepath)