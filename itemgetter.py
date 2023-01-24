from operator import itemgetter
list = [
    {"name":"Shivam", "age":20},
    {"name":"Nilesh", "age":22},
    {"name":"Sam", "age":20},
    {"name":"Nim", "age":20}
]
print(sorted(list, key=itemgetter('age','name')))
print(sorted(list, key=itemgetter('name','age')))
print(sorted(list, key=itemgetter('age')))
#lambda
print(sorted(list, key=lambda i: (i['age'], i['name'])))
