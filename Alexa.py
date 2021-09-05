import speech_recognition as sr
import pyttsx3
import pywintypes
import pywhatkit
import datetime
import wikipedia
import pyjokes
from googletrans import Translator
import webbrowser
from googlesearch import search


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.say("Welcome I am alexa")
engine.say("What can i do for you")
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "Alexa" in command:
                command = command.replace("Alexa","")
                talk(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    #Play song
    if "play" in command:
        song = command.replace("play","")
        talk("playing"+ song)
        pywhatkit.playonyt(song)
    #Time
    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("Current time is "+ time)
    #Who is person:
    elif "who is " in command:
        person = command.replace("who is" ,"")
        info = wikipedia.summary(person, 1)
        pywhatkit.search(info)
        T=Translator().translate(info,dest="hi")
        print(T)
        talk(T)
    #For going on date
    elif "date" in command:
        date = command.replace("date", "ghumne", "")
        talk("Sorry, I can not go",date)
    #Joke
    elif "joke" in command:
        jo = command.replace("joke", "chutkula", "")
        talk(pyjokes.get_joke()+jo)
    #Dance
    elif "dance" in command:
        dance = command.replace("Dance", "")
        talk("No")
   
    #open
    elif "open" in command:
        i=search(command)
        pywhatkit.search(i)
        
    else:
        talk("Say again")
while True:
    run_alexa()
