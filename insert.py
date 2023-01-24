dict = {'a':1, 'b':2}
dict.update({'c': 3,'g':5})
dict['d'] = 4
print(dict)

from collections import OrderedDict
iniordered_dict = OrderedDict([('x', '1'), ('y', '2')])
iniordered_dict.update({'z':'5'})

print(iniordered_dict)