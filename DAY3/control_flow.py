## if else

height= 120
if height > 100:
    print("Height is > 100")
else:
    print("Height is < 100")


## Modulo operators
# 0
print(10%5)

# 1
print(10%3)


## Nested if else
height= 120
if height > 100:
    print("Height is > 100")
    if height > 110:
        print("Height is > 110")
    else:
        print("Height is between 100 and 110")
else:
    print("Height is < 100")


## elif
height= 120
if height > 100:
    print("Height is > 100")
elif height > 90:
    print("Height is > 90")
elif height > 80:
        print("Height is > 80")
else:
    print("Height is : " + str(height))

## Logical Operators and
height= 120
if height > 100 and height > 110:
    print("Height is > 110")
else:
    print("Height is < 100")

## Logical Operators or
height= 120
if height > 100 or height > 110:
    print("Height is > 110")
else:
    print("Height is < 100")

## Logical Operators not
height= 120
if not height > 100 :
    print("Height is > 110")
else:
    print("Height is < 100")