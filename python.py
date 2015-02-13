# Range
assert [1, 2, 3] == [i for i in range(1, 4)]
assert [0, 1, 2] == [i for i in range(3)]


# How to use variables as a function parameter
def function(foo):
    return foo

param = 'foo'
assert function(foo='bar') == function(**{param: 'bar'})


# Partials
# Awesome article on partials:
# http://chriskiehl.com/article/Cleaner-coding-through-partially-applied-functions/
from functools import partial

def add(x, y):
    return x + y

add_five = partial(add, 5)
assert add_five(1) == 6

add_five = partial(add, y=5)
assert add_five(1) == 6
assert add_five(x=1) == 6

add_five = partial(add, x=5)
assert add_five(y=1) == 6
