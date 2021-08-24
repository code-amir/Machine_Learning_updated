def mean_MP(s, e, q,d ):

  #Sum using for loops. We can use inbuilt NumPy Sum opeartion for better speed.
  sum = 0
  for i in range(s,e+1):
    sum +=d[i]

  #Mean
  print(sum)  
  mean = sum/(e-s+1)
  q.put(mean)
  return 