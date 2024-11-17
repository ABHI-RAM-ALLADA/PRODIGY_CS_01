def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  
            shift_base = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)  
def main():
    print("Caesar Cipher Program")
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? (q to quit): ").lower()
        if choice == 'q':
            print("Exiting the program.")
            break
        elif choice in ['e', 'd']:
            message = input("Enter the message: ")
            shift = int(input("Enter the shift value (0-25): "))
            if choice == 'e':
                encrypted_message = caesar_cipher_encrypt(message, shift)
                print(f"Encrypted message: {encrypted_message}")
            elif choice == 'd':
                decrypted_message = caesar_cipher_decrypt(message, shift)
                print(f"Decrypted message: {decrypted_message}")
        else:
            print("Invalid choice. Please enter 'e' for encrypt, 'd' for decrypt, or 'q' to quit.")

if __name__ == "__main__":
    main()