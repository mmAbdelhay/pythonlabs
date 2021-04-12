# import textwrap
# textwrap.wrap(str, len)
str = input("please enter you string: ")
n = int(len(str) / 2)
if len(str) % 2 == 0:
    chunks = [str[i:i+n] for i in range(0, len(str), n)]
else:
    chunks = [str[i:i + n] for i in range(0, len(str), n)]
    chunks[0]= chunks[0]+chunks[2]
    chunks.pop()

print(chunks)

