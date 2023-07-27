def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text


def decrypt(text, shift):
    return encrypt(text, -shift)


def encrypt_file(input_file, output_file, shift):
    with open(input_file, 'r') as file:
        text = file.read()

    encrypted_text = encrypt(text, shift)

    with open(output_file, 'w') as file:
        file.write(encrypted_text)


def decrypt_file(input_file, output_file, shift):
    encrypt_file(input_file, output_file, -shift)


if __name__ == "__main__":
    try:
        input_file = input("Enter the path of the input text file: ")
        output_file = input("Enter the path of the output text file: ")
        shift = int(input("Enter the shift value for encryption/decryption: "))

        encrypt_file(input_file, output_file, shift)
        print("Encryption successful!")

        # To decrypt, uncomment the following lines:
        # decrypt_file(output_file, "decrypted_" + input_file, shift)
        # print("Decryption successful! Decrypted file saved as 'decrypted_" + input_file + "'")

    except ValueError:
        print("Invalid input. Please enter a valid shift value.")
    except KeyboardInterrupt:
        print("\nProgram interrupted.")
    except Exception as e:
        print(f"An error occurred: {e}")
