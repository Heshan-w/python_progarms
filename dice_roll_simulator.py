from random import randint;

def dice_roller(value):
    print("\nRolling.....")
    result = randint(1,value)
    return result


while True:
    try:
        sides = int(input("How many sides does the die have ?\nEnter value : "))
        print(f"Value from dice roll : {dice_roller(sides)}")    
    except ValueError:
        print("Enter an integer value\n")

    while True:
        status = input("\nTo roll again press '1'\nTo quit press 'q'\nEnter : ")
        if status == "1":
            print(f"Value from dice roll : {dice_roller(sides)}")
        elif status == "q":
            quit()
        else:
            print("Invalid input, please re-enter\n")
            continue
