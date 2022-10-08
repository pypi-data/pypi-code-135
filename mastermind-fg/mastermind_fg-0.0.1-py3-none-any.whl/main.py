import time
from Randomfunctionwork import Random_Function

start = time.time() 
print('Welcome to MASTER MIND!!!')
Difficulty = int(input("choose your game difficulty level it should be between 4 to 9 :"))
Random_number = Random_Function(Difficulty)

print("You should Guess the number which is",Difficulty ,"digit number tell me your guess:" ,end=' ')
Guess_number = str(input())
while len(Guess_number) != Difficulty:
    print('You should choose a',Difficulty,'digit Number guess again!',end=' ')
    Guess_number = str(input())

if (Guess_number == Random_number):
    print("OMG its unbelivable you guessed in just 1 try! You're a Mastermind!")
    print("Run Time: " + str( time.time() - start ))
else:
    ctr = 0
    while Guess_number != Random_number :
        ctr += 1
        count = 0
        dcount = 0
        correct = ['X']*Difficulty
        dcorrect = ['Z']*Difficulty
        for i in range(0, Difficulty):
            if (Guess_number[i] == Random_number[i]):
                count += 1
                correct[i] = Guess_number[i]
            elif Guess_number[i] in Random_number and Guess_number[i] != Random_number[i] :
                dcorrect[i] = Guess_number[i]
                dcount += 1

        print("you have guess",count, "number Correct and you have guess" ,dcount,"number that exist in number but in a wrong place")
        print("This is your situatuin right now, Consider it unmber in parentheses exist in correct number but they are in wrong place change it!!")
        for k in range(0, Difficulty):
                if correct[k] == 'X' and dcorrect[k] != "Z" :
                    print('(',dcorrect[k],')',end=' ')
                else:   
                    print(correct[k] ,end=' ')
        print('\n')
        Guess_number = str(input("Ill give you another chance , guess again :"))
        while len(Guess_number) != Difficulty:
            print('You should choose a',Difficulty,'digit Number guess again :',end=' ')
            Guess_number = str(input())
    if Guess_number == Random_number:
        print("You've become a Mastermind!")
        print("It took you only",ctr , "tries.")
        print("It took : " + str( time.time() - start ) , 'Secend to guess the number') 