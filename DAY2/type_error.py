# len can take string but not number
len("123")
# len(123) -> will give error

# check data type

# str
print(type("Hello"))
# int
print(type(123))
# float
print(type(123.1))
# bool
print(type(True))


#  Type conversion

print(type(int("123")))

user_name = "abc"
user_age = 10

## Error
# print(user_name + user_age)
print(user_name + str(user_age))
