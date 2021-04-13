import sys
from collections import Counter
import os

if os.path.exists(sys.argv[1]):
    f = open(sys.argv[1], 'r')
    file_data = f.read()
    split_it = file_data.split()
    Counter = Counter(split_it)
    most_occur = Counter.most_common(20)
    f = open('popular_words.txt', 'w')
    f.write(str(most_occur))
    f.close()
else:
    print("please enter the right path")
