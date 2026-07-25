def validate_isbn(isbn, length):

    # 1. check length mismatch (TEST 12 & 13)
    if length == 10 and len(isbn) != 10:
        print('ISBN-10 code should be 10 digits long.')
        return

    if length == 13 and len(isbn) != 13:
        print('ISBN-13 code should be 13 digits long.')
        return

    # 2. check invalid characters (TEST 14 & 8)
    if length == 10:
        if not (isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1] == 'X')):
            print('Invalid character was found.')
            return
    else:
        if not isbn.isdigit():
            print('Invalid character was found.')
            return

    # 3. split digits
    main_digits = isbn[:length - 1]
    given_check_digit = isbn[length - 1]

    main_digits_list = [int(d) for d in main_digits]

    # 4. calculate checksum
    if length == 10:
        expected = calculate_check_digit_10(main_digits_list)
    else:
        expected = calculate_check_digit_13(main_digits_list)

    # 5. result
    if given_check_digit == expected:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')


def calculate_check_digit_10(digits):
    total = 0

    for i, d in enumerate(digits):
        total += d * (10 - i)

    result = 11 - (total % 11)

    if result == 11:
        return '0'
    elif result == 10:
        return 'X'
    else:
        return str(result)


def calculate_check_digit_13(digits):
    total = 0

    for i, d in enumerate(digits):
        if i % 2 == 0:
            total += d
        else:
            total += d * 3

    result = 10 - (total % 10)

    return '0' if result == 10 else str(result)


def main():
    user_input = input('Enter ISBN and length: ')

    # format check
    if ',' not in user_input:
        print('Enter comma-separated values.')
        return

    isbn, length_str = user_input.split(',')

    # length parsing
    try:
        length = int(length_str)
    except ValueError:
        print('Length must be a number.')
        return

    # allowed lengths
    if length not in (10, 13):
        print('Length should be 10 or 13.')
        return

    validate_isbn(isbn, length)


if __name__ == '__main__':
    main()
