
# Range stuff
assert [1, 2, 3] == [i for i in range(1, 4)]
assert [0, 1, 2] == [i for i in range(3)]


# How to use variables as a function parameter
def function(foo):
    return foo

param = 'foo'
assert function(foo='bar') == function(**{param: 'bar'})
