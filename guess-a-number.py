import random
#you can change diaposone in my case this is "10"
number = random.randint(1,10)
#you can control your tries
tries = 0
print("Do you want to play ")
while tries < 6:
    my_number = int(input("Guess number: "))
    tries = tries + 1
    if my_number < number:
        print("your number is too low")
    if my_number > number:
        print("your number is too high")
    if my_number == number:
        print(f"CONGRATULAATIONS you won with {tries} tries")
    if my_number != number and tries == 6:
        print("I am soryy you lose")