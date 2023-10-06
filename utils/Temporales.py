def tokenize(exp):
    tokens = []
    i = 0
    while i < len(exp):
        if exp[i].isalnum():
            j = i
            while j < len(exp) and (exp[j].isalnum() or exp[j].isdigit()):
                j += 1
            tokens.append(exp[i:j])
            i = j
        elif exp[i] in ['+', '-', '*', '/', '(', ')']:
            tokens.append(exp[i])
            i += 1
        else:
            i += 1  # Ignorar otros caracteres, como espacios en blanco
    return tokens

def infix_to_postfix(tokens):
    def get_precedence(op):
        precedence = {'+':1, '-':1, '*':2, '/':2, '(':0, ')':0}
        return precedence[op] if op in precedence else 0

    def is_operator(c):
        return c in ['+', '-', '*', '/']

    output = []
    stack = []

    for token in tokens:
        if token.isalnum():  # Operand
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '('
        elif is_operator(token):
            while stack and get_precedence(stack[-1]) >= get_precedence(token):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output

def generate_intermediate_code(exp, result_name):
    tokens = tokenize(exp)
    postfix = infix_to_postfix(tokens)
    stack = []
    temp_counter = 1
    operations = []

    for token in postfix:
        if token.isalnum():
            stack.append(token)
        else:
            right_operand = stack.pop()
            left_operand = stack.pop()
            temp_var = f't{temp_counter}'
            operations.append(f'{temp_var} = {left_operand} {token} {right_operand}')
            stack.append(temp_var)
            temp_counter += 1

    operations.append(f'{result_name} = {stack[0]}')
    return '\n'.join(operations)
