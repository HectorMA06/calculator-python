# Basic Python Calculator

A simple command-line calculator built in Python. This project was created while I was learning Python, coming from a Java background.

> **Status:** work in progress. Right now it's just terminal-based while I get comfortable with core Python concepts. A visual (GUI) version is planned once I'm more confident.

## Description

The program asks the user for two numbers and an operation to perform, then prints the result.

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Modulo (remainder)

## How It Works

The project has two files:

### `functions.py`

Contains one function for each math operation (`add`, `substract`, `multiplication`, `division`, `modulo`). Each function takes two numbers and returns an already-formatted result string.

### `calculator.py`

This is the main file you run. It:

1. Asks the user to enter two numbers.
2. Shows a menu with the available operations.
3. Uses a **dictionary** to map each menu option to its matching function in `functions.py`.
4. Checks if the chosen option exists in the dictionary, calls the matching function, and prints the result.

It also handles some common errors:

- If the user types something that isn't a number, it shows a message instead of crashing.
- If the user tries to divide by zero, it shows a message instead of crashing.
- If the user picks an option that isn't in the menu, it shows a message instead of crashing.

## How to Run

```bash
python calculator.py
```

Then follow the prompts in the terminal.

## Example

```
This is a basic calculator using Python
Introduce the first number: 10
Introduce the second number: 5
 - 1. Sum 
 - 2. Rest 
 - 3. Multiplication 
 - 4. Divition 
 - 5. Module 
 Select the function: 1
The add of 10 + 5 is 15
```

## What I Learned

Coming from Java, this project helped me get used to:

- Python's simpler syntax (no semicolons, no curly braces).
- How Python handles input with `input()` (everything comes in as a string).
- Using `try`/`except` for error handling instead of Java's `try`/`catch`.
- Splitting code into separate files and importing them with `import`.
- f-strings for formatting output text.
- **Storing functions as values in a dictionary** (`{1: functions.add, ...}`), similar to a `Map<Integer, Function>` in Java, and calling them dynamically instead of writing a long `if`/`elif` chain.
- Using `in` to check if a key exists in a dictionary, similar to `.containsKey()` in Java.

## Possible Improvements

- Let the user run more than one calculation without restarting the program.
- Add a GUI version (planned).
- Add a history of past calculations saved to a file.
- Use custom exceptions for invalid menu options instead of a plain `else` message.

## Author

Héctor Mula Águeda
