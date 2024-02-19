#7 write a program take a string and returns most frequent characters in it.
str1=input("Enter one string :")

newstring=str()
str1=str1.lower()
i=0

for x in str1:
    if x in str1 and str1.count(x)>1:
      newstring= newstring +x

print("most frequent char :"+ newstring)