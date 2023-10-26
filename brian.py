"""
Lab 6: Software Engineering
Encode Function by: Brian Paz
Class: COP3502C
Section Number: "22282"
Description: The program will encode eight-digit by shifting the digits up by three.
"""


def encode_password(password):
    # The encoded will initialize the string to contain the shifted digits
    encoded = ""
    for integer in password:
        # The if statement will account for numbers potentially having two-digits
        if "7" <= integer <= "9":
            # 7 to 0, 8 to 1, and 9 to 2
            encoded += str((int(integer) - 7))
        # The else statement will regularly shift the number
        else:
            encoded += str(int(integer) + 3)
    return encoded


def main():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
    choice = int(input("\nPlease enter an option: "))
    while choice != 3:
        if choice == 1:
            password = input("Please enter your password to encode: ")
            encoded = encode_password(password)
            print("Your password has been encoded and stored!")
        elif choice == 2:
            print(f"The encoded password is {encoded}, and the original password is {password}.")
        print("\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        choice = int(input("\nPlease enter an option: "))

if __name__ == "__main__":
    main()
