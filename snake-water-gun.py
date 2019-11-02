import random
str_ch = ("s", "w", "g")

print("#"*5, "  Welcome to Snake Water Gun Game  ", "#"*5)
print("Game discription :: ")
print("1. You will got 10 chances")
print("2. You will have to enter : \n\ts for Snake\n\tw for Water\n\tg for Gun")
print("\nSo let's begin the game\n")

count = 0
syscount = 10
i=0
while i<10:
    print("Chance no. : ", i+1)
    player = input("Your selection : ")
    sys = random.choice(str_ch)
    if  sys == player:
        print("tie")

    else:
        if sys == 's' and player == 'w':
            print("You loose this time !")

        elif sys == 's' and player == 'g':
            print("You win this time")
            count = count + 1
            syscount = syscount - 1

        elif sys == 'w':
            if player == 's':
                print("You win this time")
                count = count + 1
                syscount = syscount - 1
            else:
                print("You loose this time")

        elif sys == 'g':
            if player == 's':
                print("You loose this time")
            else:
                print("You win this time")
                count = count + 1
                syscount = syscount - 1

    i = i + 1

print("You win ", count, " times")
print("So ", end="")
if syscount == count:
    print("This is tie. Both are winner")
elif syscount > count:
    print("Computer is winner and You are looser")
else:
    print("Congrats You are winner")



