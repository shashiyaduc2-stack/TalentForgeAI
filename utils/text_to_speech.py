import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")

engine.setProperty(
    "voice",
    voices[2].id
)

engine.setProperty(
    "rate",
    165
)

engine.setProperty(
    "volume",
    1.0
)

def speak(text):

    engine.say(text)

    engine.runAndWait()