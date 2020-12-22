import pyttsx3                             # text-to-speech library
import datetime as dt                      # supplies classes for manipulating date and time
import speech_recognition as sr            # for  performing  speech  recognition
import wikipedia as wiki                   # for accessing the parse data from wikipedia
import webbrowser as web                   # for opening web based documents
import os                                  # for using operating system dependent functionality


# It provides the program the voice to respond
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(dt.datetime.now().hour)
    if hour >= 4 and hour < 12:
        speak('Good Morning! Sir')
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")
    elif hour >= 18 and hour <20:
        speak("Good Evening!")
    else:
        speak("Sir, You should get some sleep now")
    speak("I'm in your service . Please tell me if you need something")

# It takes microphone input from the user and returns string output

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
    # It takes the user_voice input analyzes it and then according to the user query
    # it will use takecommand function and will run every step in ladder (until it finds the match in the input)
    try:
        print("Recognising..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)

        print("Pardon please!")
        return "None"
    return query

if __name__ == "__main__":
    wish_me()
    while True:
        query = takeCommand().lower()

        if "wikipedia" in query:
            speak("Searching Wikipedia..")
            query = query.replace("wikipedia", "")
            results = wiki.summary(query, sentences=2)
            speak(("According to wikipedia"))
            print(results)
            speak(results)
        elif "open youtube" in query:
            web.open("youtube.com")
        elif "open google" in query:
            web.open("google.com")
        elif "the time" in query:
            Curr_time = dt.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {Curr_time}")
        elif "open chrome" in query:
            ChromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(ChromePath)
        elif "play music" in query:
            music_dir = "C:\\Music"
            songs = os.listdir(music_dir)
            #print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'go to item pool' in query:
            web.open("https://itempool.com/neeldhara/live")
        elif 'open canvas' in query:
            web.open("https://canvas.instructure.com/")
        elif 'open git hub' in query:
            web.open("https://github.com/BlanK-1606/Helper-01/new/main")
        elif "quit" in query:
            speak("turning off, thanks for trusting me")
            exit()