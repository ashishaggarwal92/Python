# GLobal scope
enemy = 1

def my_function():
    result = 3*2
    # local scope
    enemy = 2
    print (enemy)
    return result

print(my_function())

print(enemy)


### Block scope
if 3 > 2:
    a = 10

# this will work and print 10
# local scope only applicable to functions
print(a)

# Modify global variables


friend = 10

print(friend)

friend = 20

print(friend)


# in function

good = 10

def my_fun():
    global good
    good = 20

my_fun()

print(good)