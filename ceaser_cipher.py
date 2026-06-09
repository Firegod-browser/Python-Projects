
def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


def main():
    print("=== Caesar Cipher Tool ===")
    mode = input("Do you want to encrypt or decrypt? (e/d): ").lower()

    if mode not in ['e', 'd']:
        print("Invalid option. Choose 'e' for encrypt or 'd' for decrypt.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift amount (e.g., 3): "))
    except ValueError:
        print("Shift must be a number.")
        return

    if mode == 'e':
        result = caesar_encrypt(message, shift)
        print("Encrypted message:", result)
    else:
        result = caesar_decrypt(message, shift)
        print("Decrypted message:", result)

if __name__ == "__main__":
    main()
