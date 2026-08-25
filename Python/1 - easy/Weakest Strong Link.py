def weakest_strong_link(strength):
    L = []
    C = []
    for i in range (len(strength)):
        min = strength[i][0]
        for j in range(len(strength[0])):
            if min >= strength[i][j]:
                min = strength[i][j]
        L.append(min)

    for i in range (len(strength[0])):
        max = strength[0][i]
        for j in range(len(strength)):
            if max <= strength[j][i]:
                max = strength[j][i]
        C.append(max)
    for a in L:
      if a in C:
        return a
    return -1