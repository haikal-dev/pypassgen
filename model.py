#!/usr/bin/python3

import argparse
import string
import random

def generate_password(length, uppercase=True, lowercase=True, digits=True, symbols=True):
    """
    Generates a random password of the specified length with the specified types of characters.
    """
    # Create a list of all characters to choose from based on the specified options
    characters = []
    if uppercase:
        characters.extend(string.ascii_uppercase)
    if lowercase:
        characters.extend(string.ascii_lowercase)
    if digits:
        characters.extend(string.digits)
    if symbols:
        characters.extend(string.punctuation)

    # Generate the password by randomly selecting characters from the list
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a random password.')
    parser.add_argument('length', type=int, help='Length of the password')
    parser.add_argument('-u', '--uppercase', action='store_true', help='Include uppercase letters')
    parser.add_argument('-l', '--lowercase', action='store_true', help='Include lowercase letters')
    parser.add_argument('-d', '--digits', action='store_true', help='Include digits')
    parser.add_argument('-s', '--symbols', action='store_true', help='Include symbols')
    args = parser.parse_args()

    # Generate the password and print it to the console
    password = generate_password(args.length, args.uppercase, args.lowercase, args.digits, args.symbols)
    print("Generated password:", password)

