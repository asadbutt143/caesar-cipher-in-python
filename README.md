Caesar Cipher in Python
This repository contains a Python implementation of the Caesar Cipher algorithm for both encryption and decryption of text.

Description
The Caesar Cipher is one of the simplest and most widely known encryption techniques. It is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

Encryption
To encrypt a message using the Caesar Cipher algorithm, each letter in the plaintext is shifted forward in the alphabet by a fixed number of positions, known as the "shift" or "key". For example, with a shift of 3, 'A' would be replaced by 'D', 'B' would become 'E', and so on.

Decryption
Decryption is the reverse process of encryption. Each letter in the ciphertext is shifted backward in the alphabet by the same number of positions to reveal the original plaintext.

Usage
To use this Python program for encrypting or decrypting text with the Caesar Cipher:

Run the program.
Choose whether you want to encrypt or decrypt a message.
Enter the message you want to process.
Provide the shift value.
The program will output the encrypted or decrypted text accordingly.
Example
Suppose we want to encrypt the message "HELLO" with a shift of 3. The encrypted text would be "KHOOR".

Note
This implementation preserves the case of the letters in the input text.
Non-alphabetic characters (such as spaces, punctuation, etc.) remain unchanged during encryption and decryption.
Feel free to explore and modify the provided Python code to suit your needs!
