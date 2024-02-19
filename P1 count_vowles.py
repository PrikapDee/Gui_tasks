##ques1 count of total no. of vowels
String ="Guvi Geeks Network Private Limited"
vowles=0

for x in String :
 if(x=='a' or x=='i' or x=='o' or x=='e'or x=='u'):
  vowles=vowles +1
         

print(vowles)

#ques 1count of each indidiual vowels
Vowel_A=0
Vowel_E=0
Vowl_I=0
Vowl_O=0
Vowl_U=0
for x in String :
    if x=='a' or x=='A' :
          Vowel_A=Vowel_A+1
          
    elif x=='i' or x=='I' :
          Vowl_I=Vowl_I+1
                
    elif x=='e' or x=='E':
         Vowel_E=Vowel_E=0+1
    elif x=='u' or x=='U' :
         Vowl_U=Vowl_U+1

    elif x=='o' or x=='O' : 
         Vowl_O=Vowl_O+1

print("A",Vowel_A,"I",Vowl_I,"O",Vowl_O,"U",Vowl_U,"E",Vowel_E)