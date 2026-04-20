# "My language supports the following features:
# Variables: Store both numbers and strings using the LET keyword (or REKA in Kinyarwanda). Example: LET x = 5 or LET name = "Tessy"
# Data Types: Two types - integers and strings. Integers are used for math operations, strings are enclosed in quotes.
# Input/Output: PRINT displays output to the screen, INPUT gets user input and stores it in variables.
# Arithmetic Operators: Addition (+), subtraction (-), multiplication (*), division (/), and modulo (%) for math operations.
# Comparison Operators: Equal to (==), greater than (>), and less than (<) for conditions.
# Control Structures: IF/THEN/ELSE/END for conditional logic, WHILE/DO/END for loops.
# String Operations: REVERSE reverses a string, PALINDROME checks if a string reads the same forwards and backwards.
# Kinyarwanda Support: All keywords have Kinyarwanda aliases (EREKA for PRINT, INJIZA for INPUT, etc.) to celebrate my Rwandan heritage."


def lexer(code):
    # Breaks code into tokens
    tokens = []
    current_token = ""
    in_string = False

    for char in code:
        if char == '"':
            current_token += char
            in_string = not in_string
            if not in_string:  # Just closed a string
                tokens.append(current_token)
                current_token = ""
        elif char in " \t\n" and not in_string:
            if current_token:
                tokens.append(current_token)
                current_token = ""
        else:
            current_token += char

    if current_token:
        tokens.append(current_token)
    return tokens


def apply_kinyarwanda_aliases(tokens):
    """Replace Kinyarwanda keywords with English equivalents"""
    keyword_map = {
        "EREKA": "PRINT",
        "INJIZA": "INPUT",
        "REKA": "LET",
        "NIBA": "IF",
        "NONEHO": "THEN",
        "ARIKO": "ELSE",
        "BYE": "END",
        "KOMEZA": "WHILE",
        "KORA": "DO",
        "INYUMA": "REVERSE",
        "PALI": "PALINDROME",
    }

    return [keyword_map.get(token.upper(), token) for token in tokens]


def evaluate_expression(tokens, start_index, variables):
    """Evaluates a math expression like '5 + 3' or 'x * 2'"""
    expr_tokens = []
    i = start_index

    # Stop at keywords or newlines
    while i < len(tokens) and tokens[i] not in [
        "THEN",
        "NONEHO",
        "DO",
        "KORA",
        "END",
        "BYE",
        "ELSE",
        "ARIKO",
        "WHILE",
        "KOMEZA",
        "IF",
        "NIBA",
        "PRINT",
        "EREKA",
        "LET",
        "REKA",
        "INPUT",
        "INJIZA",
        "REVERSE",
        "INYUMA",
        "PALINDROME",
        "PALI",
    ]:
        expr_tokens.append(tokens[i])
        i += 1

    # Replace variables with their values
    for j, tok in enumerate(expr_tokens):
        if tok in variables:
            expr_tokens[j] = str(variables[tok])

    # Join and evaluate
    expr_string = " ".join(expr_tokens)
    try:
        result = eval(expr_string)
        return result, i
    except Exception:
        # If it's a string, return it
        if expr_tokens and expr_tokens[0].startswith('"'):
            return expr_tokens[0], i
        return expr_tokens[0] if expr_tokens else 0, i


def evaluate_condition(tokens, start_index, variables):
    """Evaluates conditions like 'x > 5' or 'a == b'"""
    expr_tokens = []
    i = start_index

    # Collect tokens until THEN or DO
    while i < len(tokens) and tokens[i] not in ["THEN", "DO", "NONEHO", "KORA"]:
        expr_tokens.append(tokens[i])
        i += 1

    # Replace variables with values
    for j, tok in enumerate(expr_tokens):
        if tok in variables:
            expr_tokens[j] = str(variables[tok])

    # Build condition string
    condition = " ".join(expr_tokens)

    # Evaluate it
    try:
        result = eval(condition)
        return result, i
    except Exception:
        return False, i


def interpret(tokens, variables=None):
    if variables is None:
        variables = {}  # Store stuff like x=5, name="Tessy"

    i = 0  # Position tracker

    while i < len(tokens):
        token = tokens[i]

        if token == "PRINT":
            # Next token is what to print
            i += 1
            value = tokens[i]

            # Is it a string? (has quotes)
            if value.startswith('"') and value.endswith('"'):
                print(value[1:-1])  # Remove quotes and print
            # Is it a variable?
            elif value in variables:
                print(variables[value])
            # Is it a number?
            else:
                print(value)

        elif token == "IF":
            i += 1
            # Evaluate the condition
            condition_result, then_index = evaluate_condition(tokens, i, variables)
            i = then_index + 1  # Skip past THEN

            # Find where ELSE and END are
            else_index = None
            end_index = None
            depth = 1
            j = i

            while j < len(tokens):
                if tokens[j] == "IF":
                    depth += 1
                elif tokens[j] == "END":
                    depth -= 1
                    if depth == 0:
                        end_index = j
                        break
                elif tokens[j] == "ELSE" and depth == 1:
                    else_index = j
                j += 1

            # Run the appropriate block
            if condition_result:
                # Run THEN block
                then_tokens = tokens[i : else_index if else_index else end_index]
                interpret(then_tokens, variables)
                i = end_index
            else:
                # Run ELSE block if it exists
                if else_index:
                    else_tokens = tokens[else_index + 1 : end_index]
                    interpret(else_tokens, variables)
                i = end_index

        elif token == "LET":
            i += 1
            var_name = tokens[i]
            i += 1  # skip "="
            i += 1  # now at the value/expression

            # Evaluate the expression
            value, new_i = evaluate_expression(tokens, i, variables)

            # Store the result
            if isinstance(value, str) and value.startswith('"') and value.endswith('"'):
                variables[var_name] = value[1:-1]
            else:
                variables[var_name] = value

            i = new_i - 1  # Adjust position

        elif token == "INPUT":
            # Pattern: INPUT x
            i += 1
            var_name = tokens[i]
            user_input = input()  # Get input from user

            # Try to convert to number, if it fails keep as string
            try:
                variables[var_name] = int(user_input)
            except ValueError:
                variables[var_name] = user_input

        elif token == "REVERSE":
            # Pattern: REVERSE varname
            i += 1
            var_name = tokens[i]
            if var_name in variables:
                # Reverse the string
                variables[var_name] = variables[var_name][::-1]

        elif token == "PALINDROME":
            # Pattern: PALINDROME varname
            i += 1
            var_name = tokens[i]
            if var_name in variables:
                text = str(variables[var_name])
                if text == text[::-1]:
                    print("yes")
                else:
                    print("no")

        elif token == "WHILE":
            i += 1
            condition_start = i

            # Find DO
            while tokens[i] != "DO":
                i += 1
            do_index = i
            i += 1

            # Find matching END
            end_index = None
            depth = 1
            j = i

            while j < len(tokens):
                if tokens[j] in ["WHILE", "IF"]:
                    depth += 1
                elif tokens[j] == "END":
                    depth -= 1
                    if depth == 0:
                        end_index = j
                        break
                j += 1

            # Get the loop body
            loop_body = tokens[i:end_index]

            # Keep looping while condition is true
            while True:
                # Evaluate condition
                condition_tokens = tokens[condition_start:do_index]
                condition_result, _ = evaluate_condition(condition_tokens, 0, variables)

                if not condition_result:
                    break

                # Run loop body
                interpret(loop_body, variables)

            i = end_index
        i += 1  # Move to next token

    return


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python interpreter.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename, "r") as f:
        code = f.read()

    tokens = lexer(code)
    tokens = apply_kinyarwanda_aliases(tokens)  # Apply Kinyarwanda keyword mapping
    interpret(tokens)
