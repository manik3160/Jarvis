import speech_recognition as sr
import webbrowser
import pyttsx3
from openai import OpenAI

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(
        # api_key=# your openai key
    )
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and Google Cloud."},
            {"role": "user", "content": command},
        ]
    )
    return response.choices[0].message.content

def processCommand(c):
    output = aiProcess(c)
    print("Jarvis:", output)
    speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = r.listen(source, timeout=3, phrase_time_limit=3)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Listening to your command...")
                    audio = r.listen(source, timeout=5, phrase_time_limit=7)
                    command = r.recognize_google(audio)
                    processCommand(command)
        except Exception as e:
            print(f"Error: {e}")
