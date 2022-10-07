import controller


controller.change_voice(voice_index=1)


def speak(sentences='I am Ownkitaa'):
    controller.speak(sentences)


def ability():
    return ['Java', 'SQL', 'Speaker']


if __name__ == '__main__':
    pass
