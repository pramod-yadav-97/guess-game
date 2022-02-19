import socket
import random

Best_record=3
count=0
target=random.randint(0,100)

print()

print("      Hi "+ socket.gethostname())

print("*** Let's Start Playing ***")
print()

print("Rules : You have to input a number till you find the correct number")
print()
print("          All the Best !!                                                    Best Score : 3 guess")
print()
while 1:
    guess=int(input("Take a Guess => "))
    count=count+1

    if guess==target:
        print()
        print("*****************************************************")
        print("Congratulations "+ socket.gethostname() + " You have Won !")
        print()
        print("Your Score : " + str(count) +" guess ")
        print()
        print("*****************************************************")

        print()

        play_again=input("Want to play again (Yes/No)")

        if play_again.lower()=="yes" or play_again.lower()=="y":
            target=random.randint(0,100)
            count=0
            print()
            print(" ***** Game Restarted : Let Play !! ***** ")
            print()
            continue
        else:
            break

    elif guess<target:
        print("                       Hint : Guess Bigger Number")
    else:
        print("                       Hint : Guess Lower Number")

print("Thank You for Playing with me ! Hope to see you Again")


