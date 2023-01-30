def star(func):
    def inner(arg):
        print("*" * 30)
        func(arg)
        print("*" * 30)
    return inner

def percent(func):
    def inner(arg):
        print("%" * 30)
        func(arg)
        print("%" * 30)
    return inner

@star
@percent
def printer(message):
    print(message)

printer("Python decorators are wonderful!")