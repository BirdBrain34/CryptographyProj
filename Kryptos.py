import CryptoFunctions as crypt

def mainMenu():
    options = ["1. Aldjon Ciper", "2. Noel Cipher", "3. Vernam Cipher", "4. Mystery Cipher", "5. Exit"]
    for i in range (len(options)):
        print(options[i])

mainMenu()
choice = ''

while int(choice) != 5:
    choice = input("Enter your chosen number: ")
    if int(choice) not in range(1,6):
        print("Your number is invalid! Please input from 1 to 5.")
    elif int(choice) == 1:
        crypt.cipher1()
    elif int(choice) == 2:
        crypt.cipher2()
    elif int(choice) == 3:
        crypt.cipher3()
    elif int(choice) == 4:
        crypt.cipher4()