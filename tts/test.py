import pyttsx3
import speech_recognition as sr

def response(housework):
    s = 'sorry mom, I would '+ housework + ' later. I promise.'
    return s

# obtain audio from the microphone
r = sr.Recognizer()
engine = pyttsx3.init()

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

task = r.recognize_google(audio)

# refers to : https://pypi.org/project/pyttsx3/

print(task)
re = response(task)
engine.say(re)
engine.runAndWait()