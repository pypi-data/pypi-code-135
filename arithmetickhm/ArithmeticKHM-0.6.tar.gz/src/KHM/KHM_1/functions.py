import random


def decimal():
    number = random.random()
    stop = random.randint(1, 3)
    numberrounded = round(number, stop)
    return str(numberrounded)


def ratios(p):
    ratio_array = []
    letter_array = ['s', "x", "y", "z", "m", "l", "b", "t"]
    for i in range(4):
        ratio_array.append(random.randint(1, 100))
    selection = random.randint(0, 3)
    ratio_array[selection] = random.choice(letter_array)
    if p == 1:
        ratios_string = "\\dfrac{" + str(ratio_array[0]) + "}{" + str(ratio_array[1]) + "} = \\dfrac{" + str(
            ratio_array[2]) + "}{" + str(ratio_array[3]) + "}"
    else:
        ratios_string = str(ratio_array[0]) + ":" + str(ratio_array[1]) + "=" + str(ratio_array[2]) + ":" + str(
            ratio_array[3])
    return ratios_string


def ratio():
    number_1 = random.randint(1, 100)
    number_2 = random.randrange(number_1 * 2, 200, number_1)
    ratio_string = str(number_1) + ":" + str(number_2)
    return ratio_string
