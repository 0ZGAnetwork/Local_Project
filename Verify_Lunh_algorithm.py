def verify_card_number(digit: str):
    if not isinstance(digit, str):
        return "Input value must be a string"

    
    # digit = digit.replace(" ","").replace("-","")
    digit = digit.replace(" ","").replace("-","")
    if not digit.isdigit():
        return "INVALID!"
    
    # print(digit)
    values = []
    for char in digit:
        values.append(int(char))

    nums = []
    for i in range(len(values)-2, -1, -2):
        values[i] *= 2
        if values[i] > 9:
            values[i] -= 9
    # print(values)

    values = sum(values)
    # print(values)
    if values % 10 == 0:
        return 'VALID!'

    return 'INVALID!'


print(verify_card_number("4111-1111-1111-1111"))

