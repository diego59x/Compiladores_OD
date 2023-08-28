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
    elif var_name in symbols_table[scope]['variables']:
        return False, True
    else:
        return False, False

def validateSum(val1, val2):
    val1_type = validateValueType(val1)
    val2_type = validateValueType(val2)
    print(val1_type, val2_type)

def validateAssignVal(scope, formals, symbols_table, var_name, value_to_assign):
    isLocal, var_exists = validateScope(scope, symbols_table, formals, var_name)
    if not var_exists:
        return False, f'{ var_name } is not defined in the current scope.'
    if isLocal:
        expected_type = formals[var_name]
        valid, current_type = validateValueType(value_to_assign)
    else:
        expected_type = symbols_table[scope]['variables'][var_name]['type']
        valid, current_type = validateValueType(value_to_assign)
    
    if not valid:
        return False, current_type
    if current_type == 'Variable':
        pass
    elif expected_type != current_type:
        return False, f'{ var_name } expected type { expected_type } but got type { current_type }.'
    else:
        return True, 'Success'


