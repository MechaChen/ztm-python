# ztm-python

## Python Basics

### Expression vs Statements

- **Assignment**: the action to assign a value to a variable (e.g., `iq = 100`)
- **Expression**: a code fragment that evaluates to a value (e.g., `iq / 5`, `2 + 3`, `len("hello")`)
- **Statement**: a complete instruction that performs an action (e.g., assignment statement, expression statement, if statement)

**Relationships:**

- Assignment is a type of Statement (assignment statement)
- An Expression can be a Statement when used alone (expression statement)
- The right side of an Assignment is usually an Expression

<br />

### String COncatenation

- `<String>` + `<Int>` will not be a String, will have TypeError, not same as JavaScript

<br />

### List Slicing

- Lists are mutable

<br />

### Dictionary Keys

- Dictionary keys must be **hashable** (immutable types like int, str, tuple, frozenset). Immutable objects have stable hash values that don't change, making them reliable keys.


## Python Basics 2

### `enumerate()`

- `enumerate()` can generate tuple of list, and tuple's 0th element is index

### `while`

- if there is a `break`, the statement in `else` won't execute

### `break`, `continue`, `pass`

- if nothing here, it will throw error, therefore, we can use `pass` to do nothing without throwing error

### Our First GUI

- `print` will add `\n` so that next print will go next line, we can change it by passing 2nd parameter `end=''`

### Developer Fundamental IV

- clean
- Readability
- predictability
- DRY

### Parameters & Arguments

- Parameters: the variables defiend in the function definition
- Arguments: the actual values passed to the function

### Default Parameters and Keyword Arguments

- Keyword Arguments: the actual values passed to the function with names, and the order doesn't matter

### Docstrings: the note inside the functions

- `help()`: print the entire function detail
- `string.__doc__`: return the docstrings of a function

### `*args` and `**kwargs`

- `*args`: all remaining positional arguments, where `args` is a tuple
- `**kwargs`: all keyword arguments, where `kwargs` is a dictionary
- function parameters order: positional params, *args, default parameters, **kwargs

### Walrus Operator

- `:=` can assigns values to variables as part of a larger expression


### Scope

- Scope: what variables do I have access to?
- Python has functional scope


### Scope Rules

Scope priorities
- 1 - start with local scope
- 2 - then parent local scope
- 3 - then global scope
- 4 - then built-in python functions