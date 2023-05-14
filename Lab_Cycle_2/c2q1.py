def rabit_count(n):
  a,b,c=0,1,0
  print("Months\t\tNo of pairs of Rabitts")
  for i in range(1,n+1,1):
    if(i==1):
      print(i,"\t\t",b)
    else:
      c=a+b
      a=b
      b=c 
      print(i,"\t\t",c)
count=int(input("Enter the number of Months : "))
rabit_count(count)