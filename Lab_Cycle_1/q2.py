#Function to accept the three sides of a triangle
def inp():
  a=int(input("Enter the First side:"))
  b=int(input("Enter the Second side:"))
  c=int(input("Enter the Third side:"))
  return(a,b,c)#To return the accepted values


#Function to find the area of a Triangle
import math
def area(a,b,c):
  s=(a+b+c)/2
  area=math.sqrt(s*(s-a)*(s-b)*(s-c))
  return(area) 

print("For the first Triangle:")#Accepting first triangle sides
a1,b1,c1=inp()
print("For the second Triangle:")#Accepting second triangle sides
a2,b2,c2=inp()
ar1=area(a1,b1,c1)
ar2=area(a2,b2,c2)
tot=ar1+ar2               #To add up the total area of the two triangles
print("The Total area enclosed by both the trangles =",tot)
p1=(ar1/tot)*100          #To find the percentage contribution of triangle 1
p2=(ar2/tot)*100          #To find the percentage contribution of triangle 2
print("The percentage contribution of the first triangle=",p1)
print("The percentage contribution of the second triangle=",p2)
