# Python Overloading
This is a python module to implement the method overloading OOP concept.

## Example:

```python
>>> from overload import Overload
>>>
>>> @Overload
>>> def greet(name):
...     print(f"Hello, {name}")
>>> @Overload
>>> def greet(expr, name):
...     print(f"{expr}, {name}")
>>> greet('bari') # Output: Hello, bari
>>> greet('Hi', 'bari') # Output: Hi, bari
```
