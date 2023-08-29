string = "python is easy"

#checks if string starts with metioned word
print(string.startswith("python"))

#checks if string end with metioned word
print(string.endswith("easy"))

#remove prefix, if metioned string is not present then no change
print(string.removeprefix("python"))

#remove suffix, if metioned string is not present then no change
print(string.removesuffix("easy"))

#partitions the string on given letter, returns a tuple
print(string.partition('on'))

#reverse partitions the string on given letter, returns a tuple
print(string.rpartition('as'))
