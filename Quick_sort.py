def quick_sort(intigers: list) -> list:
    
    if len(intigers) <= 1:
        return intigers

    least_arr = []
    midd_arr = []
    greatest_arr = []

    idx = len(intigers) - 1
    pivot = intigers[idx]
    
    for element in intigers:
        if element < pivot:
            least_arr.append(element)
        elif element == pivot:
            midd_arr.append(element)
        else:
            greatest_arr.append(element)
    
    print(f"\033[33m{least_arr}\033[32m, {midd_arr}\033[31m, {greatest_arr}\033[0m")

    a = quick_sort(least_arr)
    c = quick_sort(greatest_arr)

    array = []

    for x in (a, midd_arr, c):
        array.extend(x)

    return array

print(quick_sort([1,2,3,4,5,2,12,3]))
