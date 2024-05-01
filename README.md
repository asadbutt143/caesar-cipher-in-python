# Caesar Cipher Encryption and Decryption

This Python program implements the Caesar Cipher algorithm to encrypt and decrypt text messages.

## Usage

To encrypt or decrypt a message using the Caesar Cipher algorithm:

1. Run the program.
2. Choose whether to encrypt or decrypt by entering 'e' or 'd' respectively.
3. Enter the message you want to encrypt/decrypt when prompted.
4. Enter the shift value to use for encryption/decryption.
5. View the encrypted or decrypted message.

## Code

The code for the Caesar Cipher algorithm is provided in `caesar_cipher.py`. It contains the following functions:

- `caesar_cipher_encrypt(text, shift)`: Encrypts the input `text` using the Caesar Cipher algorithm with the given `shift`.
- `caesar_cipher_decrypt(text, shift)`: Decrypts the input `text` using the Caesar Cipher algorithm with the given `shift`.

To use the code, import the functions into your Python script or interactive session and call them with the appropriate arguments.

## Example

```python
# Example usage of Caesar Cipher encryption and decryption
plaintext = "Hello, World!"
shift = 3
encrypted_text = caesar_cipher_encrypt(plaintext, shift)
print("Encrypted text:", encrypted_text)  # Output: "Khoor, Zruog!"
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)
print("Decrypted text:", decrypted_text)  # Output: "Hello, World!"
