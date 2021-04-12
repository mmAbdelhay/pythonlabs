string = input("please enter you string: ")
ch = input("enter you ch: ")
list1 = []

for i, v in enumerate(string):
    if v == ch:
        list1.append(i)
print(list1)