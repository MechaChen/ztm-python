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