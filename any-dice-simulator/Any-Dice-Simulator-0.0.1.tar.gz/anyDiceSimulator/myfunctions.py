from random import randint


def roll(roll):
    rolling = []
    numberOfRolls = int(roll.split('d')[0])
    diceCount = int(roll.split('d')[1])
    try:
        for x in range(numberOfRolls):
            print(f"Rolling die {x+1}...")
            result = randint(1, diceCount)
            print(f"Result: {result}")
            rolling.append(result)
    except Exception as err:
        print(f'I got bungled @_@ \n Error: {err}')

    return rolling, sum(rolling)


def printResult(listOfRolls, sumOfRolls):
    print(f'You rolled {listOfRolls} which has a total'
          f' of {sumOfRolls}')


def rolldice(x):
    rollList, rollTotal = roll(x)
    printResult(rollList, rollTotal)