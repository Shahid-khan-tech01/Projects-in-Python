from gtts import gTTS

text = "Hello Everyone "

tts = gTTS(text)

tts = gTTS(text=text, lang='en')

tts.save("audio.mp3")

print("Audio file created")