from encryption import encrypt_image, decrypt_image

def main():
    print("=== Pixel Encryption Project ===")

    while True:
        print("\nOptions:")
        print("1. Encrypt an Image")
        print("2. Decrypt an Image")
        print("3. Exit")

        choice = input("Enter choice (1-3): ").strip()

        if choice == '1':
            input_path = input("Path to input image: ")
            output_path = input("Path to save encrypted image: ")
            try:
                key = int(input("Enter encryption key (integer): "))
                encrypt_image(input_path, output_path, key)
            except ValueError:
                print("[!] Invalid key. Must be an integer.")
        elif choice == '2':
            input_path = input("Path to encrypted image: ")
            output_path = input("Path to save decrypted image: ")
            try:
                key = int(input("Enter decryption key (same as encryption key): "))
                decrypt_image(input_path, output_path, key)
            except ValueError:
                print("[!] Invalid key. Must be an integer.")
        elif choice == '3':
            print("Exiting. Stay secure! 👋")
            break
        else:
            print("[!] Invalid selection. Choose between 1–3.")

if __name__ == "__main__":
    main()