
import speech_recognition as sr
import pyttsx3 as speak
import pywhatkit
import wikipedia
import datetime
import pyjokes

listener = sr.Recognizer()
engine =speak.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def talk(text):
   engine.say(text)
   engine.runAndWait()

def take_command():   
    try:
        with sr.Microphone() as source:
            print("listening.......")
            voice = listener.listen(source)
            command= listener.recognize_google(voice)
            command= command.lower()
            if 'linda' in command:
              command= command.replace('linda','')
              
              print(command)
              
    except:
      pass
    return command
      

def run_linda():
   command= take_command()
   print(command)
   if 'play' in command:
      song= command.replace('play','')
      talk('playing a song'+ song)
      pywhatkit.playonyt(song)

   elif 'time' in command:
      time = datetime.datetime.now().strftime('%I: %M %p')
      print(time)
      talk('current time is '+ time)

   elif 'who is' in command:
    person =command.replace('who is','')
    info = wikipedia.summary(person,3)
    print(info)
    talk(info)

   elif 'joke' in command:
      talk(pyjokes.get_joke())
   
   else:
      talk("please repeat what you said")
   
while True:
   run_linda()

  