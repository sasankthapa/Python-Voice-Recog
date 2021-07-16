import speech_recognition as sr
import webbrowser
from importcsv import *

r=sr.Recognizer()

with sr.Microphone() as source:
    print('Speak Anything:')
    audio = r.listen(source)

    try:
        text=r.recognize_google(audio)
        print("You said: {}".format(text))
    except:
        print("Sorry could not recognize your voice.")

    text_0=text[:text.find(' ')]

    if text_0=='play':
        valid,url=find_url(text[text.find(' '):].strip())
        if valid:
            webbrowser.open(url.strip())
