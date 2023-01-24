dict = {
    "Shivam" : 2,
    "Apple" : 6,
    "Rahul" : 9,
    "Ram" : 8
}
# Method 1
myKey = list(dict.keys())
myKey.sort()

sortedDict = {i : dict[i] for i in myKey}
print(sortedDict)

# Method 2
for i in sorted(dict.keys()):
     print(i , dict[i], end=" ")
print()
# Method 3
from collections import OrderedDict
dict2 = OrderedDict(sorted(dict.items()))
print(dict2)

# Method 4
for i in sorted(dict):
    print(i, dict[i])

# Method 5
print(sorted(dict.items(), key=lambda kv : (kv[1],kv[0])))

# Method 6
from collections import OrderedDict
import numpy as np
keys = list(dict.keys())
values = list(dict.values())
sortedIdx = np.agrsort(values)
dict3 = {keys[i] : values[i] for i in sortedIdx}
print(dict3)

