def intersection(a, b):
  L = []
  for elema in a:
    for elemb in b:
      if elema == elemb and elema not in L:
        L.append(elema)
  return L