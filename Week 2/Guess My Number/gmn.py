print("Please think of a number between 0 and 100!")

low = 0
high = 100
mid = (low + high) // 2
status = None

while True:
    print("Is your secret number " + str(mid) + "?")
    status = input("Enter 'h' to indicate the guess is too high. \
Enter 'l' to indicate the guess is too low. \
Enter 'c' to indicate I guessed correctly. ")
    if status == 'c':
        print("Game over. Your secret number was:", str(mid))
        break
    elif status == 'l':
        low = mid
    elif status == 'h':
        high = mid
    else:
        print("Sorry, I did not understand your input.")
    if high - low <= 1:
        break
    mid = (low + high) // 2
        

