## for loops
fruits = ["app", "banana", "fig"]

for fruit in fruits:
    print(fruit)

print(fruits)


## highest score

students_scores = [11,12,13,31,21,22,12,45,76,80]

total_exam_score = sum(students_scores)
print(total_exam_score)

sum = 0
for score in students_scores:
    sum += score

print(sum)

### max()
print(max(students_scores))


#### range() with for loops

# print 1 to 9
for number in range(1,10):
    print(number)

# step 3 in each from 1 to 9
# it will print 1, 4, 7
for number in range(1,10, 3):
    print(number)

total= 0
for number in range(1,101):
    total += number
print(total)


#### WHILE loops
fruits = ["app", "banana", "fig"]
print(len(fruits))
lent = 0
while len(fruits) > lent:
    print(fruits[lent])
    lent = lent+1

