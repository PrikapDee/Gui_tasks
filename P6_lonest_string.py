#ques 6 longest common substring
str1=input("Enter one string :")
str2=input("Enter one string :")
newstring=str()
str1=str1.lower() 
str2=str2.lower()

for x in str1:
    if x in str2:
        newstring=newstring + x
    
    else :
        newstring= newstring + " "
   

##print(newstring)
separted_Substring=newstring.split()

print("longest common substrin:"+ max(separted_Substring))