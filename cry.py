from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("the-key-dont-delete-it.txt", "wb") as key_file:
        key_file.write(key)

def load_key():
   
    with open("the-key-dont-delete-it.txt", "rb") as key_file:
        return key_file.read()

def encrypt_message(message, key):
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    cipher = Fernet(key)
    decrypted_message = cipher.decrypt(encrypted_message).decode()
    return decrypted_message

if __name__ == "__main__":
    try:
        key = load_key()
    except FileNotFoundError:
        print("Encryption key not found. Generating new key...")
        generate_key()
        key = load_key()
        action = input("Enter 'e' to encrypt or 'd' to decrypt: ")
    
    if action.lower() == 'e':
        message = input("Enter the message to encrypt: ")
        encrypted_message = encrypt_message(message, key)
        print("Encrypted message:", encrypted_message)
    elif action.lower() == 'd':
        encrypted_message = input("Enter the encrypted message: ")
        decrypted_message = decrypt_message(encrypted_message.encode(), key)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid action. Please enter 'e' to encrypt or 'd' to decrypt.")
