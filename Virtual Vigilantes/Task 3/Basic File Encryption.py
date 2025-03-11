def caesar_cipher(text, key, encrypt=True):
    result = ""
    shift = key if encrypt else -key

    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Keep non-alphabet characters unchanged

    return result

def encrypt_file(input_file, output_file, key):
    with open(input_file, "r") as file:
        content = file.read()
    
    encrypted_content = caesar_cipher(content, key, encrypt=True)

    with open(output_file, "w") as file:
        file.write(encrypted_content)
    
    print(f"File '{input_file}' encrypted successfully as '{output_file}'.")

def decrypt_file(input_file, output_file, key):
    with open(input_file, "r") as file:
        content = file.read()
    
    decrypted_content = caesar_cipher(content, key, encrypt=False)

    with open(output_file, "w") as file:
        file.write(decrypted_content)
    
    print(f"File '{input_file}' decrypted successfully as '{output_file}'.")

# Example Usage
key = 3  # Shift value for encryption
encrypt_file("plaintext.txt", "encrypted.txt", key)
decrypt_file("encrypted.txt", "decrypted.txt", key)
