#ques 3 writea program that takes a string and retun after removing all the vowels from it
str1=input("Enter one string :")
vowels='aeiou'
newstring=str()
str1=str1.lower()

for x in str1:
    if x not in vowels:
        newstring=newstring + x
   

print("string without vowels :" + newstring)