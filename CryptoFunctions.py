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
    #RAIN CIPHER
    def caesar_shift(text): #shifts the letters depending on the lenght of the inputted word also loops back if it goes pass like letter Z
        shift = len(text) % 26 
        encrypted_text = ""
        
        for char in text:
            if char.isupper(): 
                shifted = chr(((ord(char) - ord('A') + shift) % 26) + ord('A')) 
            elif char.islower():
                shifted = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:
                shifted = char
            encrypted_text += shifted
            
        return encrypted_text, shift
    
    def caesar_unshift(text, shift): #Unshifts the word
        decrypted_text = ""
        
        for char in text:
            if char.isupper():
                unshifted = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            elif char.islower():
                unshifted = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:
                unshifted = char
            decrypted_text += unshifted
        return decrypted_text
    
    def umbrella(text): #shifts the letters with a right,left,right,left.. pattern in a stack like slots
        slots = [""] * len(text)
        left_index, right_index = 0, len(text) - 1
        toggle = True
        
        for char in text:
            if toggle:
                slots[right_index] = char
                right_index -= 1
            else:
                slots[left_index] = char
                left_index += 1
            toggle = not toggle
        return ''.join(slots)
    
    def evaporate(text): #undos the shifts from the umbrella function 
        left_index, right_index = 0, len(text) - 1
        original_text = []
        toggle = True 
        
        while left_index <= right_index:
            if toggle:
                original_text.append(text[right_index])
                right_index -= 1
            else:
                original_text.append(text[left_index])
                left_index += 1
            toggle = not toggle
        return ''.join(original_text)
    
    def to_droplet(text): #changes word to binary
        return ' '.join(format(ord(char), '08b') for char in text)
    
    def from_droplet(binary_text): #changes binary back to word
        return ''.join(chr(int(b, 2)) for b in binary_text.split())
    
    def rainfall_encrypt(text, demo=False): #for the demo mode of encryption and functions
        text = text.replace(" ", "")#remove spaces
        
        if demo:
            input("\n[Step 1: Cloud] Count and save the lenght of the word and Remove spaces ->"+ text + "\nPress Enter to continue...")
            
        shifted, shift_value = caesar_shift(text) #apply caesar shift
        if demo:
            input(f"\n[Step 2: Rain] Apply caesar shift depending on the count or length of the word inputted [+{shift_value}] -> " + shifted + "\nPress Enter to continue...")
            
        scrambled = umbrella(shifted) #scrambles the word with the umbrella function
        if demo:
            input("\n[Step 3: Umbrella] Get the letters in order and shift them in a right,left pattern -> " + scrambled +"\nPress Enter to continue...")
            
        binary_output = to_droplet(scrambled) + '|' + format(shift_value, '08b')  # Use '|' as a separator / Ensure 8-bit formatting


        if demo:
            input("\n[Step 4: Droplet] Convert to binary and append shift value ->"+ binary_output +"\nPress Enter to finish Ecnrypt")
            
        return binary_output
    
    def rainfall_decrypt(binary_text,demo=False): #for the demo mode of decryption
        binary_content, binary_shift = binary_text.rsplit('|', 1)  # Split at '|'
        shift_value = int(binary_shift, 2)  # Convert shift value back to integer
        scrambled = from_droplet(binary_content)  # Convert binary back to text

        
        scrambled = from_droplet(binary_content)
        if demo:
            input("\n[Step 1: Mist] Convert Binary to text ->"+ scrambled +"\nPress Enter to continue...")
            
        unscrambled = evaporate(scrambled)
        if demo:
            input("\n[Step 2: Evaporate] Reverse the shift by taking letters at the end of right,left and put them in order one by one ->"+ unscrambled +"\nPress Enter to continue...")
 
        original_text = caesar_unshift(unscrambled, shift_value)
        if demo:
            input(f"\n[Step 3: Cloud]: Reverse the caesar (-{shift_value}) ->"+ original_text +"\nPress Enter to finish Decrypt...")
        return original_text
    
    while True:
        print("\nRainfall Cipher")
        mode_choice = input("Choose mode:\n[1.] Perform Cipher\n[2.] Demo Mode \nEnter 1 or 2: ").strip()

        if mode_choice == "1":
            user_choice = input("Do you want to [E]ncrypt or [D]ecrypt: ").strip().upper()

            if user_choice == "E":
                plaintext = input("Enter the word to encrypt: ").strip()
                encrypted = rainfall_encrypt(plaintext)
                print(f"\nEncrypted Binary: {encrypted}")

                decrypt_choice = input("\nDo you want to decrypt it back [y]es or [n]o?: ").strip().upper()
                if decrypt_choice == "Y":
                    decrypted = rainfall_decrypt(encrypted)
                    print(f"Decrypted Text: {decrypted}")

            elif user_choice == "D":
                binary_input = input("Enter the binary text to decrypt: ").strip()
                decrypted = rainfall_decrypt(binary_input)
                print(f"Decrypted Text: {decrypted}")

            else:
                print("Invalid choice.")

        elif mode_choice == "2":  # Demo Mode
            user_choice = input("Do you want to [E]ncrypt or [D]ecrypt?: ").strip().upper()

            if user_choice == "E":
                plaintext = input("Enter the word to encrypt: ").strip()
                print("\nStarting Encryption Demo...")
                encrypted = rainfall_encrypt(plaintext, demo=True)
                print(f"\nFinal Encrypted Binary: {encrypted}")
                
            elif user_choice == "D":
                binary_input = input("Enter the binary text to decrypt: ").strip()
                
                print("\nStarting Decryption Demo...")
                decrypted = rainfall_decrypt(binary_input, demo=True)
                print(f"\nFinal Decrypted Text: {decrypted}")

            else:
                print("Invalid choice.")

        else:
            print("Invalid mode choice. Please enter 1 or 2.")

        continue_choice = input("\nDo you want to try again [y]es or [n]o?: ").strip().upper()
        if continue_choice != "Y":
            print("Goodbye!")
            break