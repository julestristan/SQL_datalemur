
def fizz_buzz_sum(target):
  List = []
  S    = 0
  for nb in range (3,target):
    if (nb % 3 == 0 or nb % 5 ==0):
      List.append(nb)
  for i in range(len(List)):
    S+=List[i]
  return S