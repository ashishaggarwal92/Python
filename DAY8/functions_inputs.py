## inputs with functios

def my_function(name):
    print("hi again " + str(name))
    print("how are you again")

my_function("Ashish")


## positional vs keyword argument
# positional argument
def my_function(name, location):
    print("hi again " + name)
    print("how are you again" + location)

my_function("Ashish", "Pune")



## positional vs keyword argument

# keyword argument
def my_function(name, location):
    print("hi again " + name)
    print("how are you again" + location)
    

my_function(location="Pune", name="Ashish")