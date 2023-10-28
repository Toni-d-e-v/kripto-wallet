# io.py
import os
from core.memo import create_memo
from core.crypto import encrypt, decrypt

path = "./wallets/"

def create_wallet(name, password):
    if not os.path.exists(path):
        os.makedirs(path)

    seed = create_memo()
    encrypted_seed = encrypt(seed, password)

    wallet_file = os.path.join(path, name + ".key")  # Use .key extension for wallet files
    with open(wallet_file, 'wb') as file:
        file.write(encrypted_seed)

def load_wallet(name, password):
    wallet_file = os.path.join(path, name + ".key")  # Use .key extension for wallet files
    if os.path.exists(wallet_file):
        with open(wallet_file, 'rb') as file:
            encrypted_seed = file.read()
            decrypted_seed = decrypt(encrypted_seed, password)
            return decrypted_seed
    else:
        print("Wallet not found.")
        return None

def get_wallets():
    wallets = []
    if os.path.exists(path):
        for filename in os.listdir(path):
            if filename.endswith(".key"):
                wallet_name = os.path.splitext(filename)[0]
                wallets.append(wallet_name)
    return wallets
def import_wallet(wallet_name, wallet_seed, wallet_password):
    wallet_file = os.path.join(path, f"{wallet_name}.key")  # Assume wallet file has a .key extension

    if os.path.exists(wallet_file):
        print("Wallet with the same name already exists.")
        return None

    try:
        encrypted_seed = encrypt(wallet_seed, wallet_password)

        with open(wallet_file, 'wb') as file:
            file.write(encrypted_seed)

        print(f'Wallet "{wallet_name}" imported successfully.')
        return encrypted_seed
    except Exception as e:
        print(f"Failed to import wallet: {e}")
        return None

if __name__ == "__main__":
    while True:
        print("1. Create Wallet")
        print("2. Load Wallet")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter wallet name: ")
            password = input("Enter your password: ")
            create_wallet(name, password)
            print("Wallet created successfully.")
        elif choice == "2":
            wallets = get_wallets()
            if wallets:
                print("Available Wallets:")
                print(", ".join(wallets))
                name = input("Enter wallet name: ")
                password = input("Enter your password: ")
                decrypted_seed = load_wallet(name, password)
                if decrypted_seed:
                    print("Decrypted Seed:", decrypted_seed)
                else:
                    print("Failed to load wallet.")
            else:
                print("No wallets found.")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
