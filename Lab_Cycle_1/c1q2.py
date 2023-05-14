#Function to accept the three sides of a triangle
def inp():
  check=0
  a=int(input("Enter the First side : "))
  b=int(input("Enter the Second side : "))
  c=int(input("Enter the Third side : "))
  while(a <= 0 or b <= 0 or c <= 0  ):
    if(a<=0):
      a=int(input("The value of the First side is less than 0, Please re-enter : "))
    if(b<=0):
      b=int(input("The value of the Second side is less than 0, Please re-enter : "))
    if(c<=0):
      c=int(input("The value of the Third side is less than 0, Please re-enter : "))
  if(a+b<=c or a+c<=b or b+c<=a): 
    print("Error:Invalid Triangle! The sum of the lengths of any two sides must be greater than the length of the third side.")
    check=1
  return(a,b,c,check)#To return the accepted values


#Function to find the area of a Triangle
import math
def area(a,b,c):
  s=(a+b+c)/2
  area=math.sqrt(s*(s-a)*(s-b)*(s-c))
  return(area) 

print("For the first Triangle:")#Accepting first triangle sides
a1,b1,c1,check1=inp()
print("For the second Triangle:")#Accepting second triangle sides
a2,b2,c2,check2=inp()
while(check1==1 or check2==1):#To check if the sides are valid
  print("Area cant be calculated for the given sides. Please try again")
  if(check1==1):
    print("For the first Triangle:")
    a1,b1,c1,check1=inp()
  if(check2==1):
    print("For the second Triangle:")
    a2,b2,c2,check2=inp()
ar1=area(a1,b1,c1)
ar2=area(a2,b2,c2)
tot=round(ar1+ar2,3)               #To add up the total area of the two triangles
print("The Total area enclosed by both the trangles =",tot)
p1=round((ar1/tot)*100,2)         #To find the percentage contribution of triangle 1
p2=round((ar2/tot)*100,2)         #To find the percentage contribution of triangle 2
print("The percentage contribution of the first triangle=",p1)
print("The percentage contribution of the second triangle=",p2)
