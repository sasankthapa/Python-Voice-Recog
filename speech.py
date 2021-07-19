import speech_recognition as sr
import webbrowser
from importcsv import *
from test_folderdriver import *

r=sr.Recognizer()

with sr.Microphone() as source:
    print('Speak Anything:')
    audio = r.listen(source)

    try:
        text=r.recognize_google(audio)
        print("You said: {}".format(text))
    except:
        print("Sorry could not recognize your voice.")

    print(text)
    if text[:text.find(' ')]=='play':
        valid,url=find_url(text[text.find(' '):].strip())
        if valid:
            webbrowser.open(url.strip())

    if text[:text.find(' ')]=='open':
        search_key=text[text.find(' '):].strip()
        valid,path=find_folder(search_key)
        print(valid,path)
        if valid:
            open_folder('explorer "%s"'%(path))
