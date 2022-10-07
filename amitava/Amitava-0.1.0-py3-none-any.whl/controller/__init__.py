import pyttsx3


voiceEngine = pyttsx3.init('sapi5')
voices = voiceEngine.getProperty('voices')


def change_voice(voice_rate=130, voice_volume=0.8, voice_index=0):
    voiceEngine.setProperty('rate', voice_rate)
    voiceEngine.setProperty('volume', voice_volume)
    voiceEngine.setProperty('voice', voices[voice_index].id)


def speak(sentences='Hi, I am Jarvis'):
    voiceEngine.say(sentences)
    voiceEngine.runAndWait()


if __name__ == '__main__':
    pass
