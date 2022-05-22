import speech_recognition as sr
from gtts import gTTS
import os

voice = ""
while True:
  r = sr.Recognizer()
  with sr.Microphone() as source:
    try:
      audio = r.listen(source)
      text = r.recognize_google(audio)
      print(text)
      if text == "pare":
        break
      text = r.recognize_google(audio)
      voice = voice + str(text)
    except:
      print("Oi, como você está?")
hr = gTTS(text=voice, Lang="pt-br", slow=False)
hr.save("1.wav")