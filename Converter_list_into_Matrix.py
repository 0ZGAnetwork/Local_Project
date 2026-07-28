def adjacency_list_to_matrix(arr:dict)->dict:
    
    size = len(arr)

    matrix = [[0] * size for x in range(size)]
    
    for key, values in arr.items():
        
        for value in values:
            matrix[key][value] = 1
    for row in matrix:
        print(row)

    return matrix

print(adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]}))
