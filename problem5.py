import re
string = input("please enter you string: ")
str = re.sub("[aeiouAEIOU]", "", string)
print(str)
