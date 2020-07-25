import pyttsx3
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
engine = pyttsx3.init()

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

task = r.recognize_google(audio)

# refers to : https://pypi.org/project/pyttsx3/

print(task)
engine.say("i will "+task+" later.")
engine.runAndWait()