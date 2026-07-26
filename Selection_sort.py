def selection_sort(arr):

    for i in range(len(arr)):

        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

print(selection_sort([33, 1, 89, 2, 67, 245]))
