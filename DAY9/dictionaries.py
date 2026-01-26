prog_dict = {
    "Bug":"123",
    "Bug_1":"1234",
    "Bug_2":"12345",
    }

print(prog_dict["Bug"])
print(prog_dict)

prog_dict["Bug_3"] = "234"

print(prog_dict)

## empty dictionary

empty_dict = {}
print(empty_dict)

## wipe an existing dict

prog_dict = {}


prog_dict_1 = {
    "Bug":"123",
    "Bug_1":"1234",
    "Bug_2":"12345",
    }

prog_dict_1["Bug_1"] = "234"

# print only keys
for dict in prog_dict_1:
    print(dict)
    
# print values
for dict in prog_dict_1:
    print(prog_dict_1[dict])


##### nesting
prog_dict = {
    "Bug":"123",
    "Bug_1":"1234",
    "Bug_2":"12345",
    }

prog_dict_1 = {
    "Bug": ["123", "456"],
    "Bug_1": ["1234", "4567"],
    }

print(prog_dict_1["Bug"])
print(prog_dict_1["Bug"][1])

##

nested_list = ["a", "b", ["c","d","e"]]
print(nested_list[2][1])
