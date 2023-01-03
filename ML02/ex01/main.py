# In this exercise you have to implement a function named what_are_the_vars which
# returns an instance of class ObjectC.
# ObjectC attributes are set via the parameters received during the instanciation. You will
# have to modify the ’instance’ ObjectC, NOT the class.
# You should take a look to getattr, setattr built-in functions.

def what_are_the_vars(*args, **kwargs):
    ''' Returns an instance of ObjectC, that has been modified'''
    obj = ObjectC()
    for i, arg in enumerate(args):
        setattr(obj, f'var_{i}', arg)
    for key, value in kwargs.items():
        if hasattr(obj, key):
            return None
        setattr(obj, key, value)
    return obj


class ObjectC(object):
    def __init__(self):
        pass


def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")


if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
    obj = what_are_the_vars(None, [])
    doom_printer(obj)
    obj = what_are_the_vars("ft_lol", "Hi")
    doom_printer(obj)
    obj = what_are_the_vars()
    doom_printer(obj)
    obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, a=10, var_0="world")
    doom_printer(obj)
    obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
    doom_printer(obj)

# https://pythonexamples.org/python-kwargs/