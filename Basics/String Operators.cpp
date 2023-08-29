#string class in Python
letter = "rishabh";
    
#printing word by word
for i in range(0,len(letter)):
    print(letter[i])
    
#slicing [start_index : end_index : steps]
s1 = "Hello World"

#start from 6th index and take all the letters till end in step of 1
s2 = s1[6::]
print(s2)

#start from 0th index and take all the letters till 5th index in step of 1
s3 = s1[0:5:]
print(s3)

#start from 0th index and take all the letters till enf od string in steps of 2
s4 = s1[0:len(s1):2]
print(s4)

#negative indexing is also possible, -1 is the last index and it decrements towards left like -1,-2...
s5 = s1[-1:-12:-1] 
print(s5)






