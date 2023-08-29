#string methods

string = "hello, how are you ??"
print(string)

#find method, index method, count method - string_name.find['substring',[start_index, end_index]] 
# start_index and end_index are optional

#returns the first occurence index of H
print(string.find('h'))

#returns the index where how starts
print(string.find('how'))

#returns the first index of h starting from 5th index and ending at 15th index
print(string.find('h',5,15))

#returns -1 if not found
print(string.find('X'))

#find the index of given word - throws exception if not found 
print(string.index('h'))

#count all the occurences
print(string.count('h',0,20))





