# len can take string but not number
len("123")
# len(123) -> will give error

# check data type

print(type("Hello"))
print(type(123))
print(type(123.1))
print(type(True))


#  Type conversion

print(type(int("123")))

user_name = "abc"
user_age = 10

## Error
# print(user_name + user_age)
print(user_name + str(user_age))
