import intSort
import random
import stringSort

## creating a string array
stringArr = ["Stalin", "Lenin", "Kris", "Zach", "Jiv", "Mike", "John"]

## creating random number of list 
randomList = []
for i in range(0,7):
    n = random.randint(1,100)
    randomList.append(n)
print(randomList)