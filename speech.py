import speech_recognition as sr
import webbrowser

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
    print(text_0)
    if text_0=='play':
        print('anotehu') 
