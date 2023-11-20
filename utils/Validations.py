import re
def validateValueType(value):
    if value == "": return False, 'Unknown Error'
    if value[0] == '"' and value[-1] == '"':
        return True, 'String'
    elif value == 'true' or value == 'false':
        return True, 'Bool'
    elif value[0] == '"' or value[-1] == '"':
        return False, 'String must be between double quotes.'
    else:
        try:
            int(value)
            return True, 'Int'
        except:
            return True, 'Variable'


def validateScope(scope, symbols_table, formals, var_name):
    # Check if variable exists in local scope
    if var_name in formals:
        return True, True
    elif scope in symbols_table and 'variables' in symbols_table[scope] and var_name in symbols_table[scope]['variables']:
        return False, True
    else:
        return False, False

def validateIfClause(scope, formals, symbols_table, condition, recursion_depth=0):
    # Protección contra referencias circulares
    if recursion_depth > 10:  # Puedes ajustar este número según tus necesidades
        return False, "Possible circular reference detected."

    valid, type = validateValueType(condition)
    if not valid:
        return False, type + '111'
    if type == 'Variable':
        # Recursivamente verifica el valor de la variable
        if condition in symbols_table[scope]['variables']:
            new_condition = symbols_table[scope]['variables'][condition]['value']
            return validateIfClause(scope, formals, symbols_table, new_condition, recursion_depth + 1)
        else:
            return False, f'{ condition } is not defined in the current scope. 2'
    elif type == 'Bool':
        return True, 'Success'
    else:
        return False, f'If clause condition must be of type Bool, got { type } instead.'

def validateSum(val1, val2, symbols_table, scope, formals):
    valid1, type1 = validateValueType(val1)
    valid2, type2 = validateValueType(val2)
    if (valid1 and valid2) and (type1 == 'Int' and type2 == 'Int'):
        return True, ''
    elif (not valid1 or not valid2):
        return False, 'Unknown Error'
    else:
        if type1 == 'Variable':
            isLocal, var_exists = validateScope(scope, symbols_table, formals, val1)
            if not var_exists:
                return False, f'{ val1 } is not defined in the current scope. 3'
            if isLocal:
                type1 = formals[val1]['typE']
            else:
                type1 = symbols_table[scope]['variables'][val1]['type']
        if type2 == 'Variable':
            isLocal, var_exists = validateScope(scope, symbols_table, formals, val2)
            if not var_exists:
                return False, f'{ val2 } is not defined in the current scope. 4'
            if isLocal:
                type2 = formals[val2]['typE']
            else:
                type2 = symbols_table[scope]['variables'][val2]['type']
    
    if type1 == 'Int' and type2 == 'Int':
        return True, ''
    else:
        if (type1 == 'Int' and type2 == 'Bool') or (type1 == 'Bool' and type2 == 'Int'):
            return True, ''
        else:
            return False, f'Cannot sum { type1 } and { type2 }.'

def validateAssignVal(scope, formals, symbols_table, var_name, value_to_assign, initial_expect='', initial_var='' ,recursion_depth=0):
    # Protección contra referencias circulares
    if recursion_depth > 10:  # Puedes ajustar este número según tus necesidades
        return False, "Possible circular reference detected."
    isLocal, var_exists = validateScope(scope, symbols_table, formals, var_name)
    if not var_exists:
        return False, f'{ var_name } is not defined in the current scope. 5'

    if isLocal:
        expected_type = formals[var_name]['typE']
        valid, current_type = validateValueType(value_to_assign)
    else:
        expected_type = symbols_table[scope]['variables'][var_name]['type']
        valid, current_type = validateValueType(value_to_assign)
    if initial_expect == '':
        new_initial_expect = expected_type
    else:
        new_initial_expect = initial_expect
    
    if initial_var == '':
        new_initial_var = var_name
    else:
        new_initial_var = initial_var

    if not valid:
        # TODO: Cambiar el mensaje de error / FIX
        return False, current_type+ '404'
    if current_type == 'Variable':
        # Recursivamente verifica el valor de la variable
        if value_to_assign in symbols_table[scope]['variables']:
            new_value_to_assign = symbols_table[scope]['variables'][value_to_assign]['value']
            return validateAssignVal(scope, formals, symbols_table, value_to_assign, new_value_to_assign, new_initial_expect, new_initial_var, recursion_depth + 1)
        elif value_to_assign in symbols_table:
            return True, ''
        elif value_to_assign in formals:
            return True, ''
        else:
            if 'methods' in symbols_table[scope] and value_to_assign in symbols_table[scope]['methods']:
                rtrn_type = symbols_table[scope]['methods'][value_to_assign]['returnType']
                to_assign_type = symbols_table[scope]['variables'][var_name]['type']
                if rtrn_type == to_assign_type:
                    return True, ''
                else:
                    return False, f'{ var_name } expected type { to_assign_type } but got type { rtrn_type }.'
            return False, f'{ value_to_assign } is not defined in the current scope UWU.'
    elif new_initial_expect != current_type:
        return False, f'{ new_initial_var } expected type { new_initial_expect } but got type { current_type }.'
    else:
        return True, 'Success'
