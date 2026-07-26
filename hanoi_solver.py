def hanoi_solver(n: int):

    if not isinstance(n, int):
        return 0

    if n < 1:
        return "[] [] []"
    
    rod1 = []
    rod2 = []
    rod3 = []    
    moves = []

    for number in range(n,0,-1): 
        rod1.append(number)
    
    moves.append(f"{rod1} {rod2} {rod3}")

    def move_once(source, target):
        level = source[-1]
        if target and target[-1] < level:
            print('illegal movement')
            return
        target.append(source.pop())
        moves.append(f"{rod1} {rod2} {rod3}")

    def hanoi(n, source, target, helper):
        if n == 1:
            move_once(source, target)
            return 
        hanoi(n-1, source, helper, target)
        move_once(source, target)
        hanoi(n-1, helper, target, source)

    hanoi(n, rod1, rod3, rod2)

    return "\n".join(moves)

    
print(hanoi_solver(2))

