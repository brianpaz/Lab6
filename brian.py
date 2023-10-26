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
