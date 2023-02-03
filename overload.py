"""
The python overloading implementation
"""

class Overload:
    """
    The base overloading class

    Example:

    >>> from overload import Overload
    >>> @Overload
    >>> def greet(name):
    ...     print(f"Hello, {name}")
    >>> @Overload
    >>> def greet(expr, name):
    ...     print(f"{expr}, {name}")
    >>> greet('bari') # Output: Hello, bari
    >>> greet('Hi', 'bari') # Output: Hi, bari
    """

    funcs = {}
    def __init__(self, func):
        self.func: function = func
        self.funcs[self.func] = self.func.__code__.co_argcount

    def __call__(self, *args):
        for func in self.funcs:
            if self.funcs[func] == len(args):
                return func(*args)
