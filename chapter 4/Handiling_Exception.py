def no_return():
    print("i am about to raise an exception ")
    raise Exception("This is an exception")
    print("I am not going to be printed")
    # This function will not return any value   
    return "I am not going to be printed"
def funny_divsion(divider):
    try:
        return 100/divider
    except ZeroDivisionError:
        return"zero is not a good idea"
def funny_divsion2(divider):
    try:
        if divider==13:
            raise ValueError("13 is not a good number")
        return 100/divider
    except (TypeError,ZeroDivisionError):
        return"zero is not a good idea"
def funny_divsion3(divider):
    try:
        if divider==13:
            raise ValueError("13 is not a good number")
        return 100/divider
    except (ZeroDivisionError):
        print("zero is not a good idea")
    except (TypeError):
        print("enter a number please")
    except (ValueError):
        print("no no no not 13")
        raise
try:
    raise ValueError("This is an argument")
except ValueError as e:
    print("The exception arguments were", e.args)
