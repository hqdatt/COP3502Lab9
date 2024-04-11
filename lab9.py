#Quang Dat Hoang

def encode_password(num: int):
    num_str = str(num)
    encoded = ''

    for digit in num_str:
        new_digit = (int(digit) + 3) % 10
        encoded += new_digit

    return int(encoded)

def decode_password(num_string: int) -> int:
    decoded = ""
    for digit in num_string:
        new_digit = (int(digit) - 3) % 10
        decoded += str(new_digit)
    return decoded

def main():
    while True:
        #display menu
        print("Menu \n------------- \n1. Encode \n2. Decode \n3. Quit \n")
        menu_selection = int(input("Please enter an option: ")) #prompt menu selection input

        #perform selected function
        if menu_selection == 3: 
            break
        elif menu_selection == 1:
            user_input = input("Please enter your password to encode: ")
            encoded = encode_password(user_input)
            print("Your password has been encoded and stored!\n")
        elif menu_selection == 2:
            decoded = decode_password(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded}.\n")
            ...


if __name__ == "__main__":
    main()