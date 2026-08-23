def convertToBase13(num):
  if num == 0:
    return "0"
  est_negatif = False
  if num < 0:
    est_negatif = True
    num = abs(num)
  num13 = ""
  base13 = "0123456789ABC"
  while num > 0:
    reste = num % 13
    num13 = num13 + base13[reste]
    num = num//13
  if est_negatif == False:
    return num13[::-1]
  if est_negatif == True:
    return ("-" + num13[::-1])