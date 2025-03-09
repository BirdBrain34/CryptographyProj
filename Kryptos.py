import CryptoFunctions as crypt

def mainMenu():
    options = ["\n1. Caesar Ciper", "2. Transposition Cipher", "3. Vernam Cipher", "4. Mystery Cipher", "5. Exit"]
    for i in range (len(options)):
        print(options[i])

choice = ''
choices = ['1','2','3','4','5']

while choice != 5:
    print("Welcome to Project Kryptos")
    mainMenu()
    choice = input("\nEnter your chosen number: ")
    if choice not in choices:
        print("Your input is invalid! Please input from 1 to 5.")
    elif choice == '1':
        crypt.cipher1()
    elif choice == '2':
        crypt.cipher2()
    elif choice == '3':
        crypt.cipher3()
    elif choice == '4':
        crypt.cipher4()
    elif choice == '5':
        print("Exiting program...")
        exit()