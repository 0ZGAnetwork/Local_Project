def square_root_bisection(number: (float,int), tolerance: (float,int)=0.01, maximum: (float,int)=10) -> (float,int):

    if number < 0 or not isinstance(number, (float,int)):
        raise ValueError("Square root of negative number is not defined in real numbers")

    if number == 0 or number == 1:
        print(f"The square root of {number} is {number}")
        return number
    
    low = 0
    high = max(1, number)

    for i in range(maximum):

        number_at_middle =  (low + high) / 2
        _value = number_at_middle * number_at_middle
        # print(_value)

        if high - low < tolerance:
            print(f"The square root of {number} is approximately {number_at_middle}")
            return number_at_middle
        
        if _value > number:
            high = number_at_middle
        else:
            low = number_at_middle
            
    print(f"Failed to converge within {maximum} iterations")
    return None
try:
    print(square_root_bisection(0.001, 1e-7, 50))
except ValueError as e:
    print("Error ",e)
