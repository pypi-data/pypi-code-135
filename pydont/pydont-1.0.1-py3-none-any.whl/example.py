from __init__ import dont

ask = input("Do you think that this is funny? (yes/no) : ")

if ask != "yes":
    dont()
else:
    print("Thank you!")
