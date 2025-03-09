import random
import os

def cipher1():
    # Aldjon Cipher
    os.system('cls')
    print("Caesar Cipher [Aldjon] selected")
    def caesar_cipher(text,shift,mode):
        result =""
        if mode == "decrypt":
            shift = -shift #for reversing the shift
            
        for char in text:
            if char.isalpha():
                shift_order = ord('A') if char.isupper() else ord ('a')
                result += chr((ord(char) - shift_order + shift ) % 26 + shift_order)
            else:
                result += char
        return result

    while True:
        mode = input("Choose mode [E]ncrypt or [D]ecrypt: ").strip().lower()
        if mode not in ["e","d"]:
            print("Invalid mode please choose E or D")
            continue
        
        text = input("\nEnter text: ")
        shift = int(input("Enter shift value: "))
        output = caesar_cipher(text, shift,mode)
        output = caesar_cipher(text, shift, "encrypt" if mode == "e" else "decrypt")
        print(f"\nResult: [{output}]")
        
        if mode == "e":
            decrypt_choice=input("Do you wanna decrypt this? [y]es or [n]o: ").strip().lower()
            
            if decrypt_choice == "y":
                decrypted_message = caesar_cipher(output,shift,"decrypt")
                print(f"\nDecrypted: [{decrypted_message}]")
                
        repeat = input("Do you wanna go again [y]es or [n]o?:").strip().lower()
        if repeat != "y":
             os.system('cls')
             break

def cipher2():
    # Noel Cipher
    print("Noel Cipher selected")

def cipher3():
    # Lance Cipher
    os.system('cls')
    print("***Vernam cipher***")
    while True:
        while True:
            plaintext = input("\nEnter the message to encrypt (Alphabet only, no numbers/symbols): ") #input plaintext to encrypt
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
