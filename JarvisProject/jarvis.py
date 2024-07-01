import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time
from PIL import Image, ImageGrab
import  pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 12 <= hour < 18:
        speak("Good afternoon sir!")
    elif hour >= 18:
        speak("Good evening sir!")
    else:
        speak("Good morning sir!")

    speak("How may I help you today...")

def takecommand():
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
        print("Say that again please.....")
        return "none"
    return query

def create_timer(minutes):
    speak(f"Setting a timer for {minutes} minutes.")
    time.sleep(minutes * 60)  # Convert minutes to seconds
    speak(f"Time's up! Your {minutes} minute timer has finished.")

if __name__ == "__main__":
    wishMe()

    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia...")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
        elif 'open my github' in query:
            webbrowser.open("https://github.com/shabaresh2003")
        elif "the time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the current time is {current_time}")
        elif "open code" in query:
            codepath = r"C:\Users\Vulloju shabaresh\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codepath)
        elif "open deeplearning projects" in query:
            codepath = r"E:\DeepLearning"
            os.startfile(codepath)

        elif "open web project" in query:
            codepath = r"E:\MernStack"
            os.startfile(codepath)

        elif "open netflix" in query:
            webbrowser.open("https://www.netflix.com/browse")

        elif "set timer" in query:
            speak("For how many minutes would you like to set the timer?")
            timer_query = takecommand().lower()

            try:
                timer_minutes = int(timer_query)
                create_timer(timer_minutes)
            except ValueError:
                speak("Sorry, I didn't catch that. Please say a valid number of minutes.")

        elif "jarvis" in query:
            speak("hey i am there tell me what can i do for you ")

        elif "finish".lower() in query.lower():
            exit()
