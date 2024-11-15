
# Python program to find phone numbers by name

A simple program that uses a Trie structure to efficiently search for phone numbers by name.

## Requrements

**Python:** Tested on version 3.12.1

## Running Program

To run the program, open your terminal and type:

```bash
  python
```

This will start the Python shell in the root directory of the project.


### Usage/Examples

Import the Phonebook class:

```python
from phone_book import Phonebook
```

Create an instance of the Phonebook:

```python
phonebook = Phonebook()
```

#### Call the functions:

Search for contacts:
- Takes one parameter (a string representing the prefix to search for).
- Returns a list of phone numbers (as strings) that match the prefix.

```python
phonebook.search_contact('A')
```

Add a contact:

- Takes two parameters of type strings first(name) second(number)
- Return bool (True when user added, False when user exists)

```python
phonebook.add_contact('Alice', '123456789')
```

## Author

- [@lakxpro](https://github.com/lakxpro)
