import pyttsx3
import speech_recognition as sr


engine = pyttsx3.init()

re = 'Let it go, let it go \
Can\'t hold it back anymore \
Let it go, let it go \
Turn away and slam the door \
I don\'t care what they\'re going to say \
Let the storm rage on \
The cold never bothered me anyway \
'

engine.say(re)
engine.runAndWait()