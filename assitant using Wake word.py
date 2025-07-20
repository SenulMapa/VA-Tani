import os
import subprocess
import webbrowser
import pyautogui
import pvporcupine
import pyaudio
import pyttsx3
import speech_recognition as sr
import numpy as np
from datetime import datetime
from groq import Groq
import tkinter as tk 
import time
import winsound

timer = 0 #variable for the timer


# Initializing the text to speach enigine 
txtSpeechEngine = pyttsx3.init()
voices = txtSpeechEngine.getProperty('voices')
txtSpeechEngine.setProperty('voice', voices[1].id)



def talkBack(text): #handles the talking back (txt to speach)
    txtSpeechEngine.say(text)
    txtSpeechEngine.runAndWait()

client = Groq(api_key="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") #put your groq api key here 
def UsingLLM(prompt): #Using LLAMA for answers
    try:
        # Create a chat completion request
        chatCompletion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }   
            ],
            model="llama3-8b-8192",
        )

        # Extract and print the response
        essay = chatCompletion.choices[0].message.content
        print(essay)#the variable name is kind of missleading (originally was supposed to be for generating essays)
        talkBack(essay)#usses text to speach to read out the answers 

    except Exception as e:
        print(f"Error occurred: {e}")
        talkBack("Sorry, I encountered an error.")

#basic commans
def open_application(path):
    os.startfile(path)

def open_notepad():
    subprocess.Popen('notepad.exe')

def open_calculator():
    subprocess.Popen('calc.exe')

def shutdown_system():
    os.system("shutdown /s /t 1")

def restart_system():
    os.system("shutdown /r /t 1")

def open_file_explorer():
    os.startfile("explorer.exe")

def open_task_manager():
    subprocess.Popen("Taskmgr.exe")

def open_control_panel():
    os.system("control panel")

def check_internet():
    try:
        response = os.system("ping google.com -n 1")
        if response == 0:
            talkBack("Internet connection is active.")
        else:
            talkBack("Internet connection is inactive.")
    except:
        talkBack("There was an error checking the internet connection.")

def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    talkBack(f"The current time is {current_time}.")

def mute_unmute_volume():
    pyautogui.press('volumemute')
    talkBack("Toggling mute.")

def close_application(name):
    os.system(f"taskkill /im {name}.exe /f")

def take_screenshot(filename):
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    print(f"Screenshot saved as {filename}")

def open_website(url):
    webbrowser.open(url)

def speechRec():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening for command...")
        
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start.")
            talkBack("Listening timed out while waiting for phrase to start.")
            return None
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            talkBack("Sorry, I didn't catch that.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            talkBack(f"Could not request results from Google Speech Recognition service; {e}")
            return None

#extra commands (chatgpt was used to write most of them since manually writing this would have taken too much time)
def perform_command(user_command):
    if "open chrome" in user_command:
        open_application("C:/Program Files/Google/Chrome/Application/chrome.exe")
        talkBack("Opening Chrome.")
    elif "open notepad" in user_command:
        open_notepad()
        talkBack("Opening Notepad.")
    elif "open calculator" in user_command:
        open_calculator()
        talkBack("Opening Calculator.")
    elif "shutdown" in user_command:
        shutdown_system()
        talkBack("Shutting down the system.")
    elif "restart" in user_command:
        restart_system()
        talkBack("Restarting the system.")
    elif "open explorer" in user_command:
        open_file_explorer()
        talkBack("Opening File Explorer.")
    elif "task manager" in user_command:
        open_task_manager()
        talkBack("Opening Task Manager.")
    elif "open control panel" in user_command:
        open_control_panel()
        talkBack("Opening Control Panel.")
    elif "check internet" in user_command:
        check_internet()
    elif "current time" in user_command or "what's the time" in user_command:
        get_time()
    elif "mute" in user_command:
        mute_unmute_volume()
    elif "close chrome" in user_command:
        close_application("chrome")
        talkBack("Closing Chrome.")
    elif "screenshot" in user_command:
        take_screenshot("screenshot.png")
        talkBack("Screenshot saved as screenshot.png.")
    elif "open google" in user_command:
        open_website("https://www.google.com")
        talkBack("Opening Google.")
    elif "open spotify" in user_command:
        open_application("C:/Users/user/AppData/Roaming/Spotify/Spotify.exe")
        talkBack("Opening Spotify.")
    elif "open youtube" in user_command:
        open_website("https://www.youtube.com")
        talkBack("Opening YouTube.")
    elif "open instagram" in user_command:
        open_website("https://www.instagram.com")
        talkBack("Opening Instagram.")
    elif "open facebook" in user_command:
        open_website("https://www.facebook.com")
        talkBack("Opening Facebook.")
    elif "open twitter" in user_command:
        open_website("https://www.twitter.com")
        talkBack("Opening Twitter.")
    elif "open reddit" in user_command:
        open_website("https://www.reddit.com")
        talkBack("Opening Reddit.")
    elif "open email" in user_command or "check email" in user_command:
        open_website("https://mail.google.com")
        talkBack("Opening Gmail.")
    elif "open news" in user_command:
        open_website("https://www.bbc.com/news")
        talkBack("Opening news website.")
    elif "open wikipedia" in user_command:
        open_website("https://www.wikipedia.org")
        talkBack("Opening Wikipedia.")
    elif "play music" in user_command:
        open_application("C:/Users/user/AppData/Roaming/Spotify/Spotify.exe")
        time.sleep(4.5)
        pyautogui.press('playpause')
        talkBack("Playing music.")
    elif "open netflix" in user_command:
        open_website("https://www.netflix.com")
        talkBack("Opening Netflix.")
    elif "open amazon" in user_command:
        open_website("https://www.amazon.com")
        talkBack("Opening Amazon.")
    elif "open zoom" in user_command:
        open_application("C:/Users/user/AppData/Roaming/Zoom/bin/Zoom.exe")
        talkBack("Opening Zoom.")
    elif "open word" in user_command:
        open_application("C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE")
        talkBack("Opening Microsoft Word.")
    elif "open excel" in user_command:
        open_application("C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE")
        talkBack("Opening Microsoft Excel.")
    elif "open powerpoint" in user_command:
        open_application("C:/Program Files/Microsoft Office/root/Office16/POWERPNT.EXE")
        talkBack("Opening Microsoft PowerPoint.")
    elif "increase volume" in user_command:
        pyautogui.press('volumeup', presses=5)
        talkBack("Increasing volume.")
    elif "decrease volume" in user_command:
        pyautogui.press('volumedown', presses=5)
        talkBack("Decreasing volume.")
    elif "pause music" in user_command or "pause video" in user_command:
        pyautogui.press('playpause')
        talkBack("Pausing media.")
    elif "play music" in user_command or "play video" in user_command or "resume" in user_command or "continue" in user_command:
        pyautogui.press('playpause')
        talkBack("Pausing media.")
    elif "stop music" in user_command:
        pyautogui.press('stop')
        talkBack("Stopping music.")
    elif "next track" in user_command:
        pyautogui.press('nexttrack')
        talkBack("Skipping to the next track.")
    elif "previous track" in user_command:
        pyautogui.press('prevtrack')
        talkBack("Going back to the previous track.")
    elif "use gpt" in user_command:
        talkBack("What would you like me to ask GPT?")
        prompt = speechRec()
        if prompt:
            UsingLLM(prompt)
    elif "conversation" in user_command:
            talkBack("Entering conversation mode")
            subd = 0
            while subd < 100:
                prompt = speechRec()
                if prompt:
                    UsingLLM(prompt)
    
                
        
        
    elif "reminder" in user_command: #basic reminder not the best method 
        talkBack("I will stop working until reminder done")
        talkBack(" please bear with us as we try to find a work around")
        talkBack("in how long would u like to be reminded in seconds")
        timer = speechRec()
        time.sleep(timer)
        talkBack("TIMER DONE")
        while gg <10:
            winsound.Beep(500)
            gg = gg +1

        
        
#the main process 
def main():
    porcupine = None
    audio_stream = None
    try:
        porcupine = pvporcupine.create(
            access_key="BC/lCgYTs5GTpVEE0zxe8JTOtZozAQjCYJTqtmXNgi5COqUgr7deow==",#Use your own access key 
            keyword_paths=[r"C:\Users\user\Downloads\Hey-Tani_en_windows_v3_0_0\Hey-Tani_en_windows_v3_0_0.ppn"]
        )
        
        pa = pyaudio.PyAudio()# Initialize PyAudio instance for capturing microphone input
        audio_stream = pa.open(# Open an audio stream with the parameters required by Porcupine
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )
        
        print("Listening for wake word...")

        while True:# Main loop to continuously listen for the wake word
            pcm = audio_stream.read(porcupine.frame_length)# Read a frame of audio data from the microphone
            pcm = np.frombuffer(pcm, dtype=np.int16)# Convert byte stream into a numpy array of 16-bit integers
            
            if porcupine.process(pcm) >= 0:# Check if the wake word has been detected
                print("Wake word detected. Listening for commands...")
                
                talkBack("Hey youuu")
                user_command = speechRec()# Listen for the user's voice command after the wake word
                if user_command:#when valid command is detected the action is carried out 
                    perform_command(user_command)
                
                    
    #handles any exceptions that occur during the wake word detection or audio proccessing 
    except Exception as e:
        print("An error occurred:", e)
    
    finally: #cleanup
        if porcupine:
            porcupine.delete()
        if audio_stream:
            audio_stream.close()
        pa.terminate()

if __name__ == "__main__":
    main()
