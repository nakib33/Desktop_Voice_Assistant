import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import datetime
import os
import smtplib
import sys
import shutil
import pyjokes
from urllib.request import urlopen
import requests, json
import winshell
import ctypes
import subprocess

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() 

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('halfblood613@gmail.com', 'you password')
    server.sendmail('halfblood613@gmail.com', to, content)
    server.close()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour <12:
       speak("Good Morning")
    elif hour >= 12 and hour <17:
        speak("Good Noon")
    elif hour >= 17 and hour <19:
        speak("Good Afternoon")
    elif hour >= 19 and hour <22:
        speak("Good Evening")
    else:
        speak("Good Evening")

    speak("Hello Sir. I am Leona. Please tell me how may I help You")


def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...") 
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)   
        # Say that again will be printed in case of improper voice  
        print("Say that again please...")   
        return "None"
    return query

if __name__=="__main__" :
    wishme()
    while True:
        query = takeCommand().lower()

        if query==0:
            continue
        if "stop" in str(query) or "exit" in str(query) or "goodbye" in str(query) or "close" in str(query):
            speak("Thanks for giving me your time")
            speak("Ok bye and take care sir")
            break
        elif 'hello' in query:
            speak("Hello Sir!")
        elif 'who are you' in query:
            speak("Hello, SIR. My Name is Leona. I am your Voice Assistant. I have been created by Nakib and Mehjabin")
            speak("Please tell me how may I help You")
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "why you came to world" in query:
            speak("Thanks to Nakib and Mehjabin. further It's a secret")

        elif 'reason for you' in query:
            speak("I was created as a artificial intelligence project by Nakib and Mehjabin")

        elif "who i am" in query:
            speak("If you talk then definately your human.")

        if 'wikipedia' in query:  
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            
        elif 'so funny' in query:
            speak("thank you sir")
        elif 'search'  in query:
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)
            #query.sleep(5)

        elif 'open youtube' in query:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("YouTube is open") 

        elif 'open facebook' in query:
            webbrowser.open_new_tab("https://www.facebook.com")
            speak("Facebook is open")
            
        elif 'open codeforces' in query:
            webbrowser.open_new_tab("https://codeforces.com/")
            speak("code forces is open")

        elif 'open google' in query:
            webbrowser.open_new_tab("https://www.google.com")
            speak("google is open")

        elif 'play my favourite song' in query:
            webbrowser.open("https://youtube.com/watch?v=2Vv-BfVoq4g")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'thank you' in query:
            speak("your Most Welcome sir....")

        elif 'open chrome' in query:
            codePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePath)
        elif 'open CodeBlocks' in query:
            codePath = "C:\\Program Files\\CodeBlocks\\codeblocks.exe"
            os.startfile(codePath)
        elif 'open visual studio' in query:
            codePath = "C:\\Users\\Rasel\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'epic games' in query:
            codePath = "C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
            os.startfile(codePath)

        elif 'play movie' in query:
            video_dir = 'G:\\HARRY POTTER'
            movies = os.listdir(video_dir)
            print(movies)    
            os.startfile(os.path.join(video_dir, movies[0]))

        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "nakibuddin33@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email") 


        elif 'recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin complete")
        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
        elif 'shutdown' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('leona.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
                speak("Done sir")
            else:
                file.write(note)
        