import random
import os

def cipher1():
    # Aldjon Cipher
    print("Aldjon Cipher selected")

def cipher2():
    # Noel Cipher
    print("Noel Cipher selected")

def cipher3():
    # Lance Cipher
    os.system('cls')
    while True:
        while True:
            plaintext = input("Enter the message to encrypt (Alphabet only, no numbers/symbols): ") #input plaintext to encrypt
            if plaintext.isalpha(): #Alphabets only 
                break
            else:
                print("Invalid input! Only alphabetic characters (A-Z, a-z) are allowed.")

        # Key text will be randomly generated via alphabets based on the lenght of the plaintext
        key = ''.join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz") for _ in plaintext)

        # Ciphertext is encrypted using XOR for p(Plaintext) and k(Key text)
        ciphertext = ''.join(chr(ord(p) ^ ord(k)) for p, k in zip(plaintext, key))

        # Display the text and their corresponding ASCII values 
        print("Plaintext: ", ' '.join(f"{p}({ord(p)})" for p in plaintext))
        print("Key Text:  ", ' '.join(f"{k}({ord(k)})" for k in key))
        print("Ciphertext (ASCII values):", ' '.join(str(ord(c)) for c in ciphertext))

        # Ask if the user wants to decrypt the message or not
        decrypt_choice = input("\nDo you want to decrypt? (Y to decrypt, N to skip): ").strip().lower()

        if decrypt_choice in ['y']:
            # Decrypt using XOR with the same key from the Key text
            decrypted_text = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(ciphertext, key))
            print("Decrypted message: ", ' '.join(f"{d}({ord(d)})" for d in decrypted_text))
        else:
            print("\nDecryption is skipped.")

        # Ask if the user wants to encrypt another message
        repeat_choice = input("\nDo you want to encrypt another message? (Y to continue, N to exit): ").strip().lower()
        if repeat_choice not in ['y']:
            os.system('cls')
            break

def cipher4():
    # Mystery Cipher (WIP)
    print("Mystery Cipher (WIP)")
