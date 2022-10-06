import random

def shuffling(someList):
    return random.sample(someList, len(someList))

def create_list(list):
    for i in range(6):
        list.append(i)

ourList = []
create_list(ourList)
print("Before shuffling: ", ourList)

ourList = shuffling(ourList)
print("After shuffling: ", ourList)