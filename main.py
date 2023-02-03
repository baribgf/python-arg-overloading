from overload import Overload

@Overload
def greet(name):
    print(f"Hello, {name}")

@Overload
def greet(expr, name):
    print(f"{expr}, {name}")

greet('bari')
greet('Hi', 'bari')
