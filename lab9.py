#Quang Dat Hoang

def encode(num: int):
    num_str = str(num)
    encoded = ''

    for digit in num_str:
        new_digit = (int(digit) + 3) % 10
        encoded += new_digit

    return int(encoded)

def main():
    ...

if __name__ == "__main__":
    main()