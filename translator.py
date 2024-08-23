#Import the libraries needed for the project
import googletrans
import speech_recognition
import gtts
import playsound

#Define Input and Output Language
input_lang = "en"
output_lang = "fr"
recognizer = speech_recognition.Recognizer()

#Recognize speech from Built-in Microphone
with speech_recognition.Microphone() as source:
    print("Speak Now")
    voice = recognizer.listen(source)
    text = recognizer.recognize_google(voice, language=output_lang)
    print(text)

#Translate from Google Translator
translator = googletrans.Translator()
translation = translator.translate(text, dest=output_lang)
print(translation.text)

#Convert the test into audio format, here in 'sound.mp3' format and play the sound at the same time
converted_audio = gtts.gTTS(translation.text, lang=output_lang)
converted_audio.save("sound.mp3")
playsound.playsound("sound.mp3")

#To get details about languages 
print(googletrans.LANGUAGES)