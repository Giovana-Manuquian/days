from os import system

system('cls')

number = int(input("Enter a number between [1-7]: "))

if(number == 1):
    print(f"{number} it's Monday")
elif(number == 2):
    print(f"{number} it's Tuesday")
elif(number == 3):
    print(f"{number} it's Wednesday")
elif(number == 4):
    print(f"{number} it's Thursday")
elif(number == 5):
    print(f"{number} it's Friday")
elif(number == 6):
    print(f"{number} it's Saturday")
elif(number == 7):
    print(f"{number} it's Sunday")
else:
    print("Please type something else")

