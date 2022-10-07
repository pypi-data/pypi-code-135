import controller


def speak(sentences='I am Ownkitaa'):
    controller.change_voice(voice_index=1)
    controller.speak(sentences)


def ability():
    return ['Java', 'SQL', 'Speaker']


if __name__ == '__main__':
    pass
