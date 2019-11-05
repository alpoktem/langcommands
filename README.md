# langcommands
Instructions for building language commands prototype app

## Python prototype
Install required packages:

```
$ pip install SpeechRecognition
$ pip install pocketsphinx
```

### Setting up a custom language in CMUSphinx
Go to CMUSphinx models directory under pocketsphinx python package and make a copy of the English model:
For anaconda installation this is: 
```
$ cd /Applications/anaconda3/lib/python3.7/site-packages/speech_recognition/pocketsphinx-data
$ cp en-US en-US-limited
$ cd en-US-limited
```

Replace `pronounciation-dictionary.dict` with the one provided in repository.

### Run
For microphone recognition, run:
```
$ python microphone_recognition.py
```

For file recognition, run:
```
$ python file_recognition.py <wavfile-path>
```

Sample wav files are in directory `recordings-wav`.

### Setting up your own language model

In your project folder, create grammar file `mygrammar.jsgf` containing your commands: 

```
#JSGF V1.0;
grammar twb;
public <basicCmd> = <command>;
<command> = (arab | arabic | kibaku);
```

Create finite state grammar with the command

```
$ sphinx_jsgf2fsg -fsg mygrammar.fsg < mygrammar.jsgf
```

Make sure you reference your new language and grammar while doing recognition under python:

```
r.recognize_sphinx(audio, language='en-US-limited', grammar=‘mygrammar.jsgf’))
```

## Javascript prototype

Install: 
- [node.js](https://nodejs.org/en/)
- [emscripten](https://emscripten.org/docs/getting_started/downloads.html#)
- [pocketsphinx.js](https://github.com/syl22-00/pocketsphinx.js)
- Cmake

### Installing and building pocketsphinx.js

```
$ git clone https://github.com/syl22-00/pocketsphinx.js.git
$ cd pocketsphinx.js
```

Edit `.gitmodules`. Replacing lines:

```
url = git@github.com:cmusphinx/sphinxbase.git
url = git@github.com:cmusphinx/pocketsphinx.git
```

with

```
url = https://github.com/cmusphinx/sphinxbase.git
url = https://github.com/cmusphinx/pocketsphinx.git
```

Load submodules:

```
$ git submodule init
$ git submodule update
```

### Langcommands demo

Pocketsphinx.js has built-in demo apps inside the `webapp` directory with already packaged acoustic models. In order to run the `langcommands demo`, place the `live_lang.html` into this folder and then run the python server that comes within pocketsphinx.js:

```
$ cp live_lang.html <path-to-pocketsphinx.js>/webapp
$ cd <path-to-pocketsphinx.js>
$ python server.py
```

`langcommands` app will be running in `http://localhost:8000/webapp/live_lang.html`

NOTE: The server needs to be run with python 2.

### Packaging your own language model with pocketsphinx.js

In order to run pocketsphinx.js on another language, you need to package the model directory into javascript files.  

```
$ cd <path-to-pocketsphinx.js>
$ mkdir build
$ cd build
$ cmake -DEMSCRIPTEN=1 -DCMAKE_TOOLCHAIN_FILE=<your-emscripten-path>/cmake/Modules/Platform/Emscripten.cmake -DHMM_BASE=<your-python-path>/site-packages/speech_recognition/pocketsphinx-data -DHMM_FOLDERS="en-US;en-US-langcommands" ..
$ make
```

More information can be found in [pocketsphinx.js README](https://github.com/syl22-00/pocketsphinx.js)
