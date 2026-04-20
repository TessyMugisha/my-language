# Kinyarwanda Programming Language Interpreter

A simple interpreted programming language with support for variables, control structures, loops, and string operations. Features Kinyarwanda keyword aliases celebrating Rwandan heritage.

## How to Run

1. Make sure you have Python 3 installed
2. Run a program: `python interpreter.py examples/helloworld.txt`

## Language Features

### Variables
Store numbers and strings:
LET x = 5
LET name = "Tessy"

### Input/Output
PRINT "Hello"
PRINT x
INPUT name

### Math Operations
LET result = 5 + 3
LET product = a * b
LET remainder = x % 2

### Comparisons
x == 5
y > 10
z < 3

### If Statements
IF x > 10 THEN
PRINT "Big"
ELSE
PRINT "Small"
END

### While Loops
LET i = 0
WHILE i < 5 DO
PRINT i
LET i = i + 1
END

### String Operations
REVERSE text
PALINDROME text

## Kinyarwanda Language Support

This interpreter supports Kinyarwanda keywords as aliases, celebrating my Rwandan heritage:

- **EREKA** → PRINT (show/display)
- **INJIZA** → INPUT (enter/input)
- **REKA** → LET (set/store)
- **NIBA** → IF (if)
- **NONEHO** → THEN (then)
- **ARIKO** → ELSE (otherwise)
- **BYE** → END (end)
- **KOMEZA** → WHILE (continue/repeat)
- **KORA** → DO (do)
- **INYUMA** → REVERSE (backwards)
- **PALI** → PALINDROME (palindrome)

### Example in Kinyarwanda:
EREKA "Muraho, Rwanda!"

### Kinyarwanda multiply example:
EREKA "Injiza numero ya mbere:"
INJIZA a
EREKA "Injiza numero ya kabiri:"
INJIZA b
REKA result = a * b
EREKA result

Both English and Kinyarwanda keywords work interchangeably.

## Keywords and Operators

**English Keywords:** PRINT, LET, INPUT, IF, THEN, ELSE, END, WHILE, DO, REVERSE, PALINDROME

**Kinyarwanda Keywords:** EREKA, REKA, INJIZA, NIBA, NONEHO, ARIKO, BYE, KOMEZA, KORA, INYUMA, PALI

**Operators:** +, -, *, /, %, ==, >, 

## Example Programs

All example programs are in the `examples/` folder:

1. **helloworld.txt** - Prints "Hello, World!"
2. **cat.txt** - Echoes user input
3. **multiply.txt** - Multiplies two numbers
4. **repeater.txt** - Repeats a character N times
5. **reverse_string.txt** - Reverses a string
6. **is_palindrome.txt** - Checks if string is a palindrome
7. **is_even.txt** - Checks if number is even or odd
8. **muraho.txt** - Hello world in Kinyarwanda

## Running Examples

```bash
python interpreter.py examples/helloworld.txt
python interpreter.py examples/multiply.txt
python interpreter.py examples/is_even.txt
python interpreter.py examples/muraho.txt
```
