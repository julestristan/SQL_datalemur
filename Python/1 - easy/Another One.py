def another_one(digits):
    i = 0
    L = []    
    while i < len(digits) and digits[-(i+1)] == 9:
        i += 1    
    if i > 0:
        for j in range(1, i+1):
            L.append(0)
        if i == len(digits):
            new_digits = [1] 
        else:
            new_digits = digits[:len(digits)-i]
            new_digits[-1] += 1
        new_digits += L
        return new_digits   
    else:
        digits[-1] += 1
        return digits