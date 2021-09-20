import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("good morning")
    elif(hour>=12 and hour<18):
        speak("good Afternoon")
    else:
        speak("good Evening")
    speak("hey Iam your assistant How can i help you")           

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.energy_threshold=600
        r.pause_threshold=0.5
        audio = r.listen(source)
    try:
        print("recognising..")
        query=r.recognize_google(audio,language='en-in')
        print("user said :",query)
    except Exception as e:
        #print(e)
        print("say that again please")
        return "None"
    return query

if __name__=="__main__":
   wishMe()
   while True:
     query = takeCommand().lower()
     if 'wikipedia' in query:
         speak('searching in wiki')
         query=query.replace("wikipedia","")
         results=wikipedia.summary(query,sentences=2)
         print(results)
         speak(results)
     if 'shut' in query:
         break;    


