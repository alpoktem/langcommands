#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
try:
    print("You said: " + r.recognize_sphinx(audio, language='en-US-langcommands', grammar='twb.jsgf'))
    #print("You said: " + r.recognize_sphinx(audio, language='en-US'))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
