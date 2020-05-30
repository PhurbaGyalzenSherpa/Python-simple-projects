import random
number = random.randrange(0,10)
# print(number)
life = 3
for i in range(4):
    if i !=3:
        print(f"Available life: {life}")
        guessed_number = int(input("Guess the number between 0 to 9: "))
    elif i == 3:
        print("You loose :(")
        break
    if number == guessed_number:
        print("yes, {} is the number.".format(number))
        break
    elif guessed_number < number and life != 1:
        print("Try higher number.")
    elif guessed_number > number and life != 1:
        print("Try smaller number.")

    life -= 1



