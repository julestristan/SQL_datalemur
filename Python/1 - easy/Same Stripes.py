def is_same_stripes(matrix):
    diagonales = {}
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            diff = i - j
            if diff not in diagonales:
                diagonales[diff] = matrix[i][j]
            elif diagonales[diff] != matrix[i][j]:
                return False
                
    return True