import speech_recognition as sr
import pyttsx3
import datetime
import os
import webbrowser

# Initialize speech recognition engine
recognizer = sr.Recognizer()

# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Select the voice you prefer

def get_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return f"The current time is {current_time}."

def open_application(application_name):
    if application_name.lower() == "notepad":
        os.startfile("C:\\Windows\\System32\\notepad.exe")
        return "Opening Notepad..."
    elif application_name.lower() == "calculator":
        os.startfile("C:\\Windows\\System32\\calc.exe")
        return "Opening Calculator..."
    elif application_name.lower() == "chrome":
        chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(chrome_path)
        return "Opening Chrome..."
    elif application_name.lower() == "firefox":
        firefox_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        os.startfile(firefox_path)
        return "Opening Firefox..."
    elif application_name.lower() == "word":
        word_path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
        os.startfile(word_path)
        return "Opening Microsoft Word..."
    elif application_name.lower() == "excel":
        excel_path = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
        os.startfile(excel_path)
        return "Opening Microsoft Excel..."
    # Add more application cases here as needed
    else:
        return "Sorry, I cannot open that application."



def search_web(query):
    query = query.replace("search", "").strip() if query else ""
    if query:
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open(search_url)
        return "Performing a web search..."
    else:
        return "Sorry, I didn't catch the search query. Please try again."

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            print("Command:", command)

            if "time" in command:
                response = get_time()
            elif "open" in command:
                # Extract the application name from the command
                application_name = command.replace("open", "").strip()
                response = open_application(application_name)
            elif "search" in command:
                # Extract the query from the command
                print("Web Search")
                query = command.replace("search", "").strip()
                response = search_web(query)
            else:
                response = "Sorry, I didn't understand that."

            print("Response:", response)
            engine.say(response)
            engine.runAndWait()

    except sr.UnknownValueError:
        print("Could not understand audio. Please try again.")
    except sr.RequestError as e:
        print(f"Error: {e}")
