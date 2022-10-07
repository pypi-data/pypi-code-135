import controller


def speak(sentences='I am Omitava'):
    controller.change_voice(voice_index=0)
    controller.speak(sentences)


def ability():
    return ['C', 'C++', 'Java', 'Python', 'SQL', 'OS', 'Networking']


if __name__ == '__main__':
    pass
