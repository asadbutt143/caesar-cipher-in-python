def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_text += chr((ord(char) - 97 + shift) % 26 + 97)
            elif char.isupper():
                encrypted_text += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                decrypted_text += chr((ord(char) - 97 - shift) % 26 + 97)
            elif char.isupper():
                decrypted_text += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    if choice == 'e':
        plaintext = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_text = caesar_cipher_encrypt(plaintext, shift)
        print("Encrypted text:", encrypted_text)
    elif choice == 'd':
        ciphertext = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_text = caesar_cipher_decrypt(ciphertext, shift)
        print("Decrypted text:", decrypted_text)
    else:
        print("Invalid choice. Please enter 'e' for encryption or 'd' for decryption.")

if __name__ == "__main__":
    main()
