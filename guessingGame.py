
number=int(input("Enter a number from 1 to 9"))
guess=(random.randInt(0,9))
chance=0
while chances < 5:
    if (guess == number):
    print("Congratulations you won")
    chance=chance+1
    else:
        print("You lost,the number is", number)

    