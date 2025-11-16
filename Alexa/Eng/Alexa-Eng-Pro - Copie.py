from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *

import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import time
import json
from playsound import playsound
import pygame.mixer
#تغير اول


def play_sound(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # هذا السطر لتحديد الصوت الثاني
    engine.say(text)
    engine.runAndWait()
    global name

def listen():
    
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        x="I am listening.."
        print(x)
        ui.id2.setText(x)
        play_sound('C:/Users/Lenovo/Desktop/Gpt/sound.mp3')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        command = ""
        try:
            command = r.recognize_google(audio, language='EG')
            print(f"You : {command}")
            ui.id1.setText(command)
        except sr.UnknownValueError:
            play_sound('C:/Users/Lenovo/Desktop/Gpt/Old Skype - Call Declined Sound Effect.mp3')
            x="Sorry, I did not understand the command."
            speak(x)
            ui.id2.setText(x)
        except sr.RequestError:
            x="Sorry, there seems to be an issue with the service."
            speak(x)
            ui.id2.setText(x)
    return command

def close_browser():
    os.system("taskkill /f /im chrome.exe")
def close_notepad():
    os.system("taskkill /f /im notepad.exe")

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
def set_volume(value):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # مستوى الصوت يتراوح بين -65 (صامت) و 0 (أعلى صوت)
    min_vol = volume.GetVolumeRange()[0]
    max_vol = volume.GetVolumeRange()[1]

    desired_volume = min_vol + (max_vol - min_vol) * value / 100.0
    volume.SetMasterVolumeLevel(desired_volume, None)
# def play_on_youtube(query):
#     webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
def play_first_video_on_youtube(query):
    from youtubesearchpython import SearchVideos

    search = SearchVideos(query, offset=1, mode="json", max_results=1)
    video_info = json.loads(search.result())
    video_link = video_info["search_result"][0]["link"]
    webbrowser.open(video_link)
    
def main():
    r = sr.Recognizer()
    speak('welcome ,Ziad')
    while True: # هذه الحلقة الخارجية ستستمر دائمًا
        wake_command_received = False #ON/OFF

        # Listen for the wake command first
        while not wake_command_received:
            with sr.Microphone() as source:
                print("Listening for the wake-up command ...")
                print("say Alixa to wake up")
                audio = r.listen(source)

                try:
                    command = r.recognize_google(audio, language='EG')
                    print(f"You : {command}")
                    if "Alexa" in command:
                        wake_command_received = True
                        speak("Activated!,How can I assist you today?")
                except sr.UnknownValueError:
                    pass

        name = ""

        # هذه الحلقة ستستمر حتى تقول "good bye" أو "go to sleep"
        while wake_command_received:
            command = listen().lower()

            if "good bye" in command or "go to sleep" in command or "goodbye" in command:
                speak("If you need help, tell Alexa to activate!")
                speak("GoodBye"+name)
                play_sound('C:/Users/Lenovo/Desktop/Gpt/Old Skype - Going Offline Sound Effect.mp3')
                break

                wake_command_received = False
            elif "break" in command :
                speak("Countdown to closing")
                speak("5")
                speak("4")
                speak("3")
                speak("2")
                speak("1")
                speak('Deactivate')
                play_sound('C:/Users/Lenovo/Desktop/Gpt/Old Skype - Going Offline Sound Effect.mp3')
                break
                

            elif "restart computer" in command:
                os.system("shutdown /r /t 1")
                speak("Restarting the computer!")
                
            elif "shut down computer" in command:
                os.system("shutdown /s /t 5")
                speak("Shutting down the computer!")
                
            elif "take a screenshot" in command:
                from datetime import datetime
                import pyautogui
                current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')  # الحصول على الوقت والتاريخ الحالي
                screenshot_path = r'C:\Users\Lenovo\Pictures\Screenshots\Screenshot_' + current_time + '.png'

                screenshot = pyautogui.screenshot()
                screenshot.save(screenshot_path)
                speak(f"Screenshot taken and saved as {screenshot_path}")
            
            elif "play youtube" in command or "youtube" in command:
                 import pyautogui as pg
                 speak("What song or video do you want me to play?")
                 query = listen()
                 play_first_video_on_youtube(query)
                 
            elif "stop" in command or "play" in command:
                 import pyautogui as pg
                 pg.press('playpause')
                 speak('done')
                
            elif "next" in command:
                import pyautogui as pg
                speak("Moved to the next track.")
                pg.press('nexttrack')

            elif "back" in command or "go back" in command:
                import pyautogui as pg
                speak("Moved to the previous track.")
                pg.press('prevtrack')
            elif "volume down" in command:
                import pyautogui as pg
                for i in range(8):  # يقوم بتخفيض الصوت 20 مرة
                    pg.press('volumedown')
                speak("Volume lowered.")
                
            elif "volume min" in command or "volume minimum" in command:
                import pyautogui as pg
                set_volume(1)
                speak("minimum Volume ")
                
            elif "volume medium" in command or "medium" in command:
                import pyautogui as pg
                set_volume(89.1)
                speak("Medium Volume .")
                
            
                
            elif "volume max" in command or "max" in command:
                import pyautogui as pg
                set_volume(100)
                speak("Max Volume.")
                
            elif "volume up" in command:
                import pyautogui as pg
                for i in range(8):  # يقوم برفع الصوت 25 مرة
                    pg.press('volumeup')
                speak("Volume raised.")
                
                
            elif "play spotify" in command or "open spotify" in command:
                import pyautogui as pg
                speak("Playing Spotify!")
                os.system("start spotify")
                time.sleep(2)  # إعطاء التطبيق بعض الوقت ليتم فتحه
                pg.press('playpause')
                
            elif "what is the time" in command:
                from datetime import datetime
                current_time = datetime.now().strftime("%H:%M")
                speak(f"The current time is {current_time}")
                
            elif "play youtube" in command and "play YouTube" in command:
                speak("What song or video do you want me to play?")
                query = listen()
                play_on_youtube(query)
                speak("done")

            #-------------------------------------------------------------            


            #Apps
                
            #-------------------------------------------------------------
            #Open
            elif "open notepad" in command:
                os.system("notepad.exe")
                speak("Notepad opened!")
            elif "open google" in command:
                webbrowser.open('http://www.google.com')
                speak("Google opened! ")
                
                
            #close
            elif "close notepad" in command:
                close_notepad()
                speak("Notepad closed!")
            
            elif "close google" in command:
                close_browser()
                speak("google closed!")

            #-------------------------------------------------------------            
            #communication
            elif "do you know my name" in command:
                if len(name) > 1:
                    speak("Yes, your name is " + name)
                else:
                    speak("No, what is your name?.")
                    name = listen()
                    speak("Nice to meet you, " + name )

                
            elif "i love you" in command:
                speak("i love you too,")
            
            elif "hello" in command or "hi" in command:
                speak("Hello again!")
                             
            elif "how are you" in command:
                speak("I'm just a program, so I don't have feelings, but thanks for asking!")

            else:
                x=speak("I apologize, I did not catch that.")
                x=speak("If you don't want me to talk, say goodbye and I will deactivate")
                ui.id2.setText(x)
                
app = QApplication([])
ui = loadUi ("StartScript.ui")
ui.show()   
if __name__ == "__main__":
    main()
    


app.exec_()    