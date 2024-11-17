Functions:
caesar_cipher_encrypt: This function takes a string and a shift amount. It shifts characters as appropriately based on the shift value while preserving the case of the letters. 
Therefore, caesar_cipher_decrypt: Simply calls the encrypt function with a negative shift to decrypt the provided string. 
Main Loop:
This program prompts the user for a choice to encrypt a message, decrypt a message, or quit.
This does exactly the same thing as procedure above : it takes a message and a shift value as argument, then prints out the result accordingly.
Usage:
Run the program, then either encrypt or decrypt a message following the prompts.
You can use any shift value from 0 up to 25; the program will handle the wrapping around the alphabet.
Note:
Non-alphabetic characters (spaces, punctuation, etc.) are not affected by encryption or decryption.
