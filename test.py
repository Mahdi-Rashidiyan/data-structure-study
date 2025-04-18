def guess_number():
    print("Think of a number between 0 and 100")
    lower = 0
    upper = 100
    found = False

    while not found:
        guess = (lower + upper) // 2
        print(f"\nMy guess is: {guess}")
        response = input("Is this correct? (Y/M/L)\nY - Yes!\nM - My number is More\nL - My number is Less\n").upper()

        if response == 'Y':
            print(f"\nGreat! Your number is {guess}!")
            found = True
        elif response == 'M':
            lower = guess + 1
        elif response == 'L':
            upper = guess - 1
        else:
            print("Please enter Y, M, or L")

        if lower > upper:
            print("You must have made a mistake somewhere!")
            break

guess_number()





