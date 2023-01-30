# ChainingDecorators
Chaining Decorators is really amazing in Python, it's a function that can be decorated with the same or multiple decorators:

# In this case we have a Star function with another fuction inside this function that allows it to add functionalities to this function and return it:

def star(func):
    def inner(arg):
        print("*" * 30)
        func(arg)
        print("*" * 30)
    return inner

# Same below:

def percent(func):
    def inner(arg):
        print("%" * 30)
        func(arg)
        print("%" * 30)
    return inner

# Now with the @ symbol makes it more readable and also the intentions of this program clear, the star functions embrace the percent function that embraces the printer function:

@star
@percent
def printer(message):
    print(message)

# here we call this funciton and it´ll use the decorators accordingly:

printer("Python decorators are wonderful!")
