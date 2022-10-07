import controller


def speak(sentences='I am Onikyt'):
    controller.change_voice(voice_index=0)
    controller.speak(sentences)


def ability():
    return ['Java', 'SQL']


if __name__ == '__main__':
    pass
