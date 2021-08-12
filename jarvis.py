import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os



engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning Sam how r u doing")
    elif hour<12 and hour>=17:
        speak("good afternoon Sam how r u doing")
    else:
        speak("good evening sam how r u doing")

def takecommand():
    #to take microphone command from user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
         print("Recognizing.....")
         query = r.recognize_google(audio,language='en-in')
         print(f"user said: {query}\n")

    except Exception as e:

        print("say that again.....")
        return "None"
    return  query

if __name__ == '__main__':
    wish()
    #while True:
    if 1:
        query=takecommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia.....')
            query=query.replace('wikipedia',"")
            results=wikipedia.summary(query, sentences=1)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:

            music_dr='D:\\zenfone music'
            songs=os.listdir(music_dr)
            print(songs)
            os.startfile(os.path.join(music_dr,songs[7]))

        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strtime}")

        elif 'open code' in query:
            codepath= "E:\\Program Files (x86)\\VLC"
            os.startfile(codepath)





