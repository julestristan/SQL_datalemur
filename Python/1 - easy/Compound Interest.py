def compound_interest(principal, rate, contribution, years):
  total = 0
  total = principal * (1+rate*0.01)**years + contribution * (((1+rate*0.01)**years-1)/(rate*0.01))
  return round(total,2)