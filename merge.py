# Merge 1
def mergeDict(dict1, dict2):
    return dict2.update(dict1)

dict1 = {'a':1, 'b':2, 'c':3}
dict2 = {'d':4, 'e':5, 'c':6}

mergeDict(dict1, dict2)
# print(dict2)

# Method 2 

def Merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res
     
dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}
dict3 = Merge(dict1, dict2)
print(dict3)

dict3['a'] = 20

print(dict1)
