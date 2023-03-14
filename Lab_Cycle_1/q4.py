#Function to check whether the accepted number is a happy number or not and return true or false accordingly
def check_happy(n):
  i=0#Used to check how many times the loop works
  while(n!=1):
    a,s=n,0
    while(a>0):
      r=a%10
      s=s+r*r#To add up the sum of squares of the digits
      a=a//10
    n=s#To change the value of n to the sum of squares of the digits
    i=i+1
    if(i>100):
      break
  if((n==1)and(i<100)):
    return True #Return true if it is a happy number
  else:
    return False #Return false if the number is a sad number
  
  #Function to print all the happy numbers between 2 limits
def range_happy(a,b):
  i=a
  k=0
  while(i<=b):
    bo=check_happy(i) #Calling the function to check if i is a happy number  
    if(bo==True):
      print(i," ") #If it is then print the number
      k=k+1
    i=i+1
  if(k==0):
    print("No happy numbers in this limit.")

    #Function to print all the happy number til the accepted limit
def happy_n(n):
  i=0
  c=0
  while(c<n):
    bo=check_happy(i)#Calling the function to check if i is a happy number
    if(bo==True):
      print(i," ")
      c=c+1
    i=i+1

#to check whether the accepted number is happy or not
n=int(input("Enter a number:"))
bo=check_happy(n)
if(bo==True):
  print("The number is a happy number")
else:
  print("The number is a sad number")

#to generate happy number between a range 
a=int(input("Enter the lower limit:"))
b=int(input("Enter the upper limit:"))
range_happy(a,b)

#to generate all the happy numbers upto a limit
n=int(input("Enter a limit:"))
happy_n(n)