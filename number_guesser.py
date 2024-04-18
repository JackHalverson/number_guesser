def number_guesser():
    low = 1
    high = 100
    guessed = False
    
    while not guessed:
        print()
        guess = (low + high) // 2
        print(f"Is it {guess}?")
        response = input("yes(y) or no(n): ").lower()
        
        if response == "y":
            print()
            print("I got it! Awesome! Thanks for playing!")
            guessed = True
        elif response == "n":
            direction = input("Was that too high(h) or too low(l): ").lower()
            if direction == "h":
                high = guess - 1
            elif direction == "l":
                low = guess + 1
        else:
            print("Please enter 'yes' or 'no'.")

number_guesser()