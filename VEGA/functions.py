import pyttsx3
import speech_recognition as sr
import datetime
import os
import pyautogui
import requests
import random
import wikipedia
import cv2
import pyjokes
import time
from requests.adapters import HTTPAdapter
from requests.adapters import Retry
from fake_useragent import UserAgent
import webbrowser
from bs4 import BeautifulSoup
import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def startup():
    speak("Hello sir, My name is VEGA, Your virtual assistant. How can I help you today?")


def takecommand():
    # it takes microphone input from users and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language="en-in")
        print("user said:", query)

    except Exception as e:
        return "None"
    query = query.lower()
    return query


def webcam():
    # Load the cascade

    # To capture video from webcam.
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    # To use a video file as input
    # cap = cv2.VideoCapture('filename.mp4')

    while True:
        # Read the frame
        _, img = cap.read()

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect the faces

        # Display
        cv2.imshow('img', img)

        # Stop if escape key is pressed
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    # Release the VideoCapture object
    cap.release()


def givenews():
    apikey = '49e391e7066c4158937096fb5e55fb5d'
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={apikey}"
    r = requests.get(url)
    data = r.json()
    data = data["articles"]
    flag = True
    count = 0
    for items in data:
        count += 1
        if count > 5:
            break
        print(items["title"])
        to_speak = items["title"].split(" - ")[0]
        if flag:
            speak("Today's top ten Headline are : ")
            flag = False
        else:
            speak("Next news :")
        speak(to_speak)


def weather(city):

    # Generating the url
    url = "https://google.com/search?q=weather+in+" + city

    # Sending HTTP request
    request_result = requests.get(url)

    # Pulling HTTP data from internet
    soup = BeautifulSoup(request_result.text, "html.parser")

    # Finding temperature in Celsius.
    # The temperature is stored inside the class "BNeawe".
    temp = soup.find("div", class_='BNeawe').text.replace("C", "celsius")
    print(temp)
    speak(f"Sir it looks like the temprature is {temp}")
