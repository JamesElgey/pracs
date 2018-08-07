### James Elgey
MIN_LENGHT = 5

def main():
    password = get_password()
    while len(password) < MIN_LENGHT:
        print("Error, password too short...")
        password = input("Enter a password:")
    print("Password accepted")
    print("*" * len(password))


def get_password():
    password = input("Enter a password:")
    return password


main()
