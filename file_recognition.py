#!/usr/bin/env python3
import speech_recognition as sr
from os import path
import sys

AUDIO_FILE = sys.argv[1]

LANG_DICT = {'hausa':'Hausa', 'haoussa':'Hausa', 
			 'barbacci':'Kanuri', 'barno':'Kanuri', 'kolejo':'Kanuri', 'buangelangela':'Kanuri', 'kanuri':'Kanuri',
			 'fulfulde': 'Fulfulde', 'fulani': 'Fulfulde', 'fulah': 'Fulfulde', 'fula': 'Fulfulde', 'fulbe': 'Fulfulde', 'fullata': 'Fulfulde', 'pullo': 'Fulfulde',
			 'shuwa':'Shuwa', 'shuwa arab':'Shuwa', 'shuwa arabic':'Shuwa', 'shuwa arab':'Shuwa', 'arab':'Shuwa', 'arabic':'Shuwa', 'chadian arabic': 'Shuwa', 'chadian arab': 'Shuwa',
			 'bura': 'Bura-Pabir', 'bura pabir':'Bura-Pabir', 'babur':'Bura-Pabir', 'pabir':'Bura-Pabir', 
			 'waha': 'Waha',
			 'chibok':'Kibaku', 'kibaku': 'Kibaku', 'kikuk':'Kibaku', 'kyibaku':'Kibaku', 'chibbak':'Kibaku', 'chibok':'Kibaku', 'cibak':'Kibaku',
			 'mandara':'Mandara', 'wandala':'Mandara', 'elvawandala':'Mandara'}

print("Listening: ", AUDIO_FILE)
print("Label: ", path.basename(AUDIO_FILE).split('-')[0][:-1])

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
	audio = r.record(source)  # read the entire audio file

# recognize speech using Sphinx
result = ""
try:
	result = r.recognize_sphinx(audio, language='en-US-langcommands', grammar='twb.jsgf')
	print("Recognized: " + result)
except sr.UnknownValueError:
	print("Sphinx could not understand audio")
except sr.RequestError as e:
	print("Sphinx error; {0}".format(e))

try:
	print("Language: " + LANG_DICT[result])
except:
	print("Unkown language")


print("==========================")
