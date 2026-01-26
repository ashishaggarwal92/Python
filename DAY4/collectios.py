fruits = ["app", "banana"]

print(fruits)
print(fruits[0])
print(len(fruits))

print(fruits[-1])

## single item adds to list
fruits.append("guaua")
print(len(fruits))

fruits.extend(["guaua","cherry"])
print(len(fruits))
print(fruits)

## index error

states_of_america = ["ABC", "DEF"]
#print(states_of_america[2])

## list with in a list / Nested list

fruits = ["apple" , "banana"]
vegetables = ["onion", "tomato"]

fruits_and_vegies = [fruits, vegetables]

print(fruits_and_vegies[0])

# print banana
print(fruits_and_vegies[0][1])