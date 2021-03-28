# Name- Romilkumar Patel
# PSID- 1765483

# roster function
def roster():
    # Data dictionary
    global data
    print("ROSTER")
    for i in sorted(data.keys()):
        print("Jersey number: " + str(i) + ", Rating: " + str(data[i]))


# Function to add new player
def addPlayer():
    global data
    jersey_number = int(input("Enter a new player's jersey number:\n"))
    # If jursey number already added or not in between 0-99
    while ((jersey_number < 0 or jersey_number > 99) or (jersey_number in data)):
        if (jersey_number in data):
            print("Already added")
        else:
            print("Enter values between 0-99 (inclusive)")
        jersey_number = int(input("Enter a new player's jersey number:\n"))
    rating = int(input("Enter player's rating:\n"))
    # If rating is not in between 1-9
    while (rating < 1 or rating > 9):
        print("Enter values between 1-9 (inclusive)")
        rating = int(input("Enter player's rating:\n"))
    data[jersey_number] = rating


# Function to remove player
def removePlayer():
    global data
    jersey_number = int(input("Enter a jersey number:\n"))
    # If jursey number not added or not in between 0-99
    while ((jersey_number < 0 or jersey_number > 99) or (jersey_number not in data)):
        if (jersey_number < 0 or jersey_number > 99):
            print("Enter values between 0-99 (inclusive)")
        else:
            print("Jersey number not added")
        jersey_number = int(input("Enter a jersey number:\n"))
    del data[jersey_number]


def updatePlayer():
    global data
    jersey_number = int(input("Enter a jersey number:\n"))
    # If jursey number not added or not in between 0-99
    while ((jersey_number < 0 or jersey_number > 99) or (jersey_number not in data)):
        if (jersey_number < 0 or jersey_number > 99):
            print("Enter values between 0-99 (inclusive)")
        else:
            print("Jersey number not added")
        jersey_number = int(input("Enter a jersey number:\n"))
    rating = int(input("Enter a new rating for player:\n"))
    # If rating is not in between 1-9
    while (rating < 1 or rating > 9):
        print("Enter values between 1-9 (inclusive)")
        rating = int(input("Enter a new rating for player:\n"))
    data[jersey_number] = rating


# To print Jersey number above given rating
def aboveRating():
    global data
    rating = int(input("Enter a rating:\n"))
    print("\nABOVE " + str(rating))
    for i in data:
        if (data[i] > rating):
            print("Jersey number: " + str(i) + ", Rating: " + str(data[i]))


# Dictionary to store values
data = {}
i = 0
# Adding 5 values
for i in range(5):
    jersey_number = int(input("Enter player " + str(i + 1) + "'s jersey number:\n"))
    # If jursey number already added or not in between 0-99
    while ((jersey_number < 0 or jersey_number > 99) or (jersey_number in data)):
        if (jersey_number in data):
            print("Already added")
        else:
            print("Enter values between 0-99 (inclusive)")
        jersey_number = int(input("Enter player " + str(i + 1) + "'s jersey number:\n"))
    rating = int(input("Enter player " + str(i + 1) + "'s rating:\n"))
    # If rating is not in between 1-9
    while (rating < 1 or rating > 9):
        print("Enter values between 1-9 (inclusive)")
        rating = int(input("Enter player " + str(i + 1) + "'s rating:\n"))
    data[jersey_number] = rating
    print("")

roster()

# Menu
choice = ""
while (True):
    print("\nMENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")

    choice = input("\nChoose an option:\n")
    choice = choice.lower()

    if (choice == "a"):
        addPlayer()
    elif (choice == "d"):
        removePlayer()
    elif (choice == "u"):
        updatePlayer()
    elif (choice == "r"):
        aboveRating()
    elif (choice == "o"):
        roster()
    elif (choice == "q"):
        break
    else:
        print("Wrong choice")