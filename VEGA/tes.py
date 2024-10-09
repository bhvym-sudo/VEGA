import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("anirudh is my sonz")