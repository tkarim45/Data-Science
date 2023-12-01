
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
voicespeed = 225
engine.setProperty('rate', voicespeed)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-PK')
    except Exception as e:
        print(e)
        print("---")

        return "None"
    return query


if __name__ == "__main__":

    while True:
        command = take_command().lower()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'who is' in command:
            person = command.replace('who the heck is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'date' in command:
            talk('sorry, I have a headache')
        elif 'are you single' in command:
            talk('I am in a relationship with wifi')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'open whatsapp' in command:
            os.system("open /Applications/WhatsApp.app")
        elif 'sleep' in command:
            break
        else:
            talk('Please say the command again.')
