import pyttsx3 as p
import speech_recognition as sr
from sel_web import Info, Music
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
import time
from time import strftime
from news import *
import randfacts 
from datetime import datetime
from temprature import *
# Speak Func
def speak(text):
    engine = p.init()
    engine.setProperty('rate', 150)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()
#listen to the voice
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 20000
        r.adjust_for_ambient_noise(source, 1.2)
        print('Listening...')
        audio = r.listen(source)
    try:
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        speak("Sorry, there was an issue with the speech recognition service.")
        return None
#greet according to Hours
def greet():
    today = datetime.now()
    hour = int(today.hour)
    if hour < 12:
        return "Good morning"
    elif 12 <= hour < 16:
        return "Good afternoon"
    else:
        return "Good evening"
#date
def get_date_time():
    today = datetime.now()
    return today.strftime('%d'), today.strftime('%B'), today.strftime('%I:%M %p')
#automate
def perform_action(command):
    driver_path = ""
    if 'information' in command:
        speak("You need information on which topic?")
        topic = listen()
        if topic:
            speak(f'Searching for {topic} on Wikipedia')
            print(f'Searching for {topic} on Wikipedia')
            assist = Info(driver_path)
            assist.get_info(topic)
            try:
                while True:
                    time.sleep(1)
                    try:
                        assist.driver.current_url
                    except WebDriverException:
                        break
            except KeyboardInterrupt:
                pass
            finally:
                assist.driver.quit()
    elif 'play' in command and 'video' in command:
        speak('Which video do you want to watch?')
        vid = listen()
        if vid:
            speak(f"Searching for {vid} on YouTube")
            print(f"Searching for {vid} on YouTube")
            assist2 = Music(driver_path)
            assist2.play(vid)
    elif 'news' in command:
        speak("Sure sir")
        all_news = new_s()
        for news in all_news:
            speak(news)
    elif 'facts' in command or 'fact' in command:
        speak("Sure sir")
        fact = randfacts.get_fact()
        speak(f'Do you know that {fact}')
    elif 'time' in command:
        speak("The current time is " + str(datetime.now().strftime("%H:%M:%S")))
        print("The current time is " + str(datetime.now().strftime("%H:%M:%S")))
    elif 'temperature' in command:
        temperature = temp()
        speak("The current temperature in Islamabad is " + str(temperature) + ' Celsius.')
        print("The current temperature in Islamabad is " + str(temperature) + ' Celsius.')
    elif 'Quit' in command or 'exit' in command:
        speak("Goodbye sir")
        print("Goodbye sir")
        return False
    return True

def main():
    speak("Hello Sir, " + greet() + ", I am your voice assistant. How are you?")
    day, month, time_str = get_date_time()
    speak(f'Today is {day} of {month} and it is currently {time_str}')
    response = listen()
    if response and 'what' in response and 'about' in response and 'you' in response:
        speak("I am also having a good day, sir.")
    
    while True:
        speak('What can I do for you?')
        command = listen()
        if command:
            if not perform_action(command):
                break

if __name__ == "__main__":
    main()
