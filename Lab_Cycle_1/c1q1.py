#Function to return the sum of digits of a number
def sum( n):
  s=0
  while(n>0):
    r=n%10;#To seperate each digits
    s=s+r#To store the sum
    n=n//10
  return s

#Function to return the reverse of a number
def reverse(n):
  s=0
  while(n>0):
    r=n%10#To seperate each digit
    s=s*10+r#To store the reverese of a number
    n=n//10
  return(s)

"""Function to find the difference between the product of digits at the odd 
postion and the product of digits at the even postions"""
def prod(n):
  s,a,b=0,1,1
  i=1
  while(n>0):
    r=n%10
    if(i%2==0):#To check for even and odd positions of the digit
      b=b*r#To store the product of digits in even places
    else:
      a=a*r#To store the product of digits in odd places
    i=i+1
    n=n//10
  s=b-a#To find the difference of even and odd places
  return(s)

n=int(input("Enter a 4 digit number:"))
while (n<1000 or n>9999):
  n=int(input("Invalid input, Please enter a 4 digit number : "))
s=sum(n)#To call the sum functio
print("The Sum of Digits=",s)
r=reverse(n)#To call the reverse function
print("The Reverse of the number=",r)
s1=prod(n)#To call the prod function
print("The difference of product of even and odd numbers=",s1)