from collections import OrderedDict
def checkOrder(input, pattern):
    dict = OrderedDict.fromkeys(input)
    patlen = 0
    # print(dict)
    for key, value in dict.items():
        if(key == pattern[patlen]):
        # if (key == pattern[ptrlen]): 

            patlen = patlen+1

        if(patlen == len(pattern)):
            return 'true'
    
    return 'false'


pattern = input("Enter the pattern ")
input = input("Enter the input ")
ans = checkOrder(input, pattern)
print(ans)







# from collections import OrderedDict
# def checkOrder(input, pattern):
#     dict = OrderedDict.fromkeys(input)
#     patlen = 0
#     print(dict)
#     # for key, value in dict.item():

# pattern = input("Enter the pattern ")
# input = input("Enter the input ")
# checkOrder(input, pattern)

