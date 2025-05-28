import string
import random

# Getting password length
length = int(input("Enter password length: "))

print('''Choose character set for password from these: 
         1. Letters
         2. Digits
         3. Special characters
         4. Done selecting''')

characterList = ""

# Getting character set for password
while True:
    choice = int(input("Pick a number: "))
    if choice == 1:
        characterList += string.ascii_letters  # A-Z, a-z
    elif choice == 2:
        characterList += string.digits         # 0-9
    elif choice == 3:
        characterList += string.punctuation    # Special characters
    elif choice == 4:
        if characterList == "":
            print("You must select at least one character set.")
        else:
            break
    else:
        print("Please pick a valid option!")

# Generate password
password = [random.choice(characterList) for _ in range(length)]

# Print password
print("The random password is:", "".join(password))
