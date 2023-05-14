#Function to print all the possible substrings
def all_subs(s):
  i,j=0,0
  l=len(s)#To find the length of the accepted string
  for i in range(0,l+1):
    for j in range(i+1,l+1):
      print(s[i:j],end=",")#To print all the substrings


#Function to print all possible substrings of length n
def subs_with_length(s,n):
  i,j=0,0
  l=len(s)
  for i in range(0,l+1):
    for j in range(i+1,l+1):
      s1=s[i:j]#To store the substring values to check if the length is equal to n
      if(len(s1)==n):
        print(s1,end=",")


#Function to print all possible substings of length n with c distinct characters
def subs_dist_char_and_length(s,n,c):
  i,j=0,0
  l=len(s)
  for i in range(0,l+1):
    for j in range(i+1,l+1):
      s1=s[i:j]
      dist=set(s1)#To make the strings unique that is ton delete duplicate characters
      if(len(dist)<=n)and(len(dist)==c):
        print(s1,end=",")


#Function to print all possible substings of with c distinct characters
def subs_dist_char_and_max_length(s,n,c):
  i,j=0,0
  l=len(s)
  for i in range(0,l+1):
    for j in range(i+1,l+1):
      s1=s[i:j]
      dist=set(s1)#To make the strings unique that is to delete duplicate characters
      if(len(dist)==c):
        print(s1,end=",")


#Function to print all palindrome substrings
def print_palindrome_subs(s):
  i,j=0,0
  l=len(s)
  for i in range(0,l+1):
    for j in range(i+1,l+1):
      s1=s[i:j]
      s2=s1[::-1]#To reverse the substring
      if(s2==s1):
        print(s1,end=",")
  

s=input("Enter the String:")
print("All possible substrings are:")
all_subs(s)

k=int(input("\nEnter the length of the substrings that you want to print:"))
print("The possible substrings with length",k,"is:")
subs_with_length(s,k)