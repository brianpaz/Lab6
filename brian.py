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

# by bari walters
def decode(encoded):
    # creates a string to add the reduced digits to
    empty_string = ""
    # goes through each digit in encoded password
    for digit in encoded:
        # subtracts 3 from each digit
        empty_string += str(int(digit) - 3)
        # accounts for numbers that will be negative when subtracting 3
        if "0" <= digit <= "2":
            # removes negative number from string
            empty_string = empty_string[:-2]
            # adds the negative number plus 7 (to make it positive) to the string
            empty_string += str(int(digit) + 7)

    return empty_string


def main():

    encoded = "00000000"
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
    choice = int(input("\nPlease enter an option: "))

    # The while loop will exit when the user wants to stop coding passwords
    while choice != 3:
        # The if statement will account for encoding the user-given password
        if choice == 1:
            password = input("Please enter your password to encode: ")
            encoded = encode_password(password)
            print("Your password has been encoded and stored!")
        # The elif statement will account for decoding the user-given password and displaying both
        elif choice == 2:
            print(f"The encoded password is {encoded}, and the original password is {decode(encoded)}.")
        print("\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        choice = int(input("\nPlease enter an option: "))


if __name__ == "__main__":
    main()
