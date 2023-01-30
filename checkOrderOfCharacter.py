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

inp = input("Enter the input ")
pattern = input("Enter the pattern ")

ans = checkOrder(inp, pattern)
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

