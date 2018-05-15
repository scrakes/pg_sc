import win32com.client as wincl
import pyautogui as pg
import webbrowser as wb

speak = wincl.Dispatch("SAPI.SpVoice")

speak.Speak("What is your favorite animal?")

answer = pg.prompt("Enter your favorite animal below.")

if answer == "giraffe":
    speak.Speak("YASSSSSSSSS.")
elif answer == "dolphin":
    speak.Speak("Noice.")
elif answer == "wolf":
    speak.Speak("You have my respect.")
else:
    speak.Speak("This is a gucci choice.")

speak.Speak("What video do you want to look up?")

video = pg.prompt("Enter video below.")

speak.Speak("Ok, let's go look for " + video + " on YouTube.")

wb.open("https://www.youtube.com/results?search_query=" + video)
