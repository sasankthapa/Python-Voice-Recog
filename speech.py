import speech_recognition as sr
import webbrowser
from importcsv import *
from test_folderdriver import *
from test_volumedriver import *
from test_webdriver import *

r=sr.Recognizer()

while True:
    def listen_to_voice():
        with sr.Microphone() as source:

            print('Speak Anything:')
            audio = r.listen(source)
            voice_data=''

            try:
                text=r.recognize_google(audio)
                print("You said: {}".format(text))
            except:
                return 1;
                print("Sorry could not recognize your voice.")

            if text[:text.find(' ')]=='play':
                valid,url=find_url(text[text.find(' '):].strip())
                if valid:
                    webbrowser.open(url.strip())

            if text[:text.find(' ')]=='open':
                search_key=text[text.find(' '):].strip()
                valid,path=find_folder(search_key)
                if valid:
                    open_folder('explorer "%s"'%(path))
                    
            if text[:text.find(' ')]=='set':
                search_key=text[text.find(' '):].strip()
                if search_key=='volume zero':
                    change_volume(0)

            if text[:text.find(' ')]=='hey':
                google(text[text.find(' '):].strip())

    listen_to_voice()
#    print('How can I help you?');
#    print(voice_data)

#voice_data=record_audio()
