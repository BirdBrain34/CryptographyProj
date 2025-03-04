def mainMenu():
    options = ["1. Aldjon Ciper", "2. Noel Cipher", "3. Vernam Cipher", "4. Mystery Cipher", "5. Exit"]
    for i in range (len(options)):
        print(options[i])

mainMenu()
choice = input("Enter your chosen number: ")