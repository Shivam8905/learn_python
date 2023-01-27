num1 = int(input("Enter start range:"))
num2 = int(input("Enter end range:"))

number = [*range(num1, num2+1)]
square = [value ** 2 for value in number]

database = dict(zip(number, square))

counter=0
mySet = set()

while  counter<3:
    find = int(input("Your database is ready, Enter the number you want to search "))
    if find in database and find not in mySet:
        print(database[find])
        mySet.add(find)
    elif find not in database and counter<=3:
        print("You have chosen a value which is not in database " + str(counter+1) +"times wrong")
        counter = counter+1
    elif find in mySet:
        print("You have already searched for this number "  + str(counter+1) +"times wrong")
        counter = counter+1
    

        
