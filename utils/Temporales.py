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

class Temporales(object):
    def __init__(self) -> None:
        self.temporals = {

        }
        pass

    def check_all_temps_used(self, fun_context):
        if (self.temporals[fun_context]["last_temporal"] == 9):
            for i in range(0, 8):
               self.temporals[fun_context]["reusable_temps"].append(i)

    def exists(self, fun_context, temporal):
        if fun_context in self.temporals[fun_context]:
            if temporal in self.temporals[fun_context][temporal]:
                return True
        return False
    
    def free_temporal(self, fun_context, temporal):
        # if (not "reusable_temps" in self.temporals[fun_context])
        self.temporals[fun_context]["reusable_temps"].append(temporal)

    def get_correct_id(self, fun_context):
        if (not fun_context in self.temporals):
            self.temporals[fun_context] = {
                "last_temporal": 0,
                "reusable_temps":[]
            }

        if ("reusable_temps" in self.temporals[fun_context]):
            if (len(self.temporals[fun_context]["reusable_temps"]) > 0):
                return self.temporals[fun_context]["reusable_temps"].pop()
        
        self.check_all_temps_used(fun_context)
        self.temporals[fun_context]["last_temporal"] = self.temporals[fun_context]["last_temporal"] + 1
        return self.temporals[fun_context]["last_temporal"]

    def get_last_id(self, fun_context):
        return self.temporals[fun_context]["last_temporal"]
    
    def get_temporal(self, fun_context, temporal, content):
        if (not fun_context in self.temporals):
            self.temporals[fun_context] = {
                "last_temporal": 0,
                "reusable_temps":[]
            }

        for temporal in self.temporals[fun_context]:
            if (temporal not in ["last_temporal", "reusable_temps"] and self.temporals[fun_context][temporal] in content):
                return temporal
            
    def set_double_temporal(self, fun_context, temporal, left, right):
        existing_temporal1 = self.get_temporal(fun_context, temporal, left)
        existing_temporal2 = self.get_temporal(fun_context, temporal, right)

        if (existing_temporal1 != None or existing_temporal2 != None):
            left = left.replace(self.temporals[fun_context][existing_temporal1], existing_temporal1)
            self.temporals[fun_context][temporal] = left

            right = right.replace(self.temporals[fun_context][existing_temporal2], existing_temporal2)
            self.temporals[fun_context][temporal] = right

            if (existing_temporal2 == right or existing_temporal1 == left):
                return ''
            return f' {temporal} {left + ", " + right}\n'
        
        self.temporals[fun_context][temporal] = left + right
        
        return f' {temporal} {left + ", " + right}\n'
            
    def set_temporal(self, fun_context, temporal, content):
        existing_temporal = self.get_temporal(fun_context, temporal, content)

        if (existing_temporal != None):
            content = content.replace(self.temporals[fun_context][existing_temporal], existing_temporal)
            self.temporals[fun_context][temporal] = content

            if (existing_temporal == content):
                return existing_temporal
            return f'{temporal}, {content}\n'
        
        self.temporals[fun_context][temporal] = content
        
        return f'{temporal}, {content}\n'
