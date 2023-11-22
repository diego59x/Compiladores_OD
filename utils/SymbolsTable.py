class SymbolsTable:
    def __init__(self):
        self.symbols_table = {}
    def addScope(self, scope):
        if scope not in self.symbols_table:
            self.symbols_table[scope] = {}
    def addInherits(self, scope, inherits):
        self.symbols_table[scope]['inherits'] = inherits
        self.symbols_table[scope]['superclass'] = inherits

        if (inherits != None):
            superclass = inherits
            while True:
                if (superclass in self.symbols_table and self.symbols_table[superclass]["inherits"] != None):
                    superclass = self.symbols_table[superclass]["inherits"]
                    self.symbols_table[scope]['superclass'] = superclass
                else:
                    break

    def addVariable(self, scope, id, typE, value, is_global=False):
        if 'variables' in self.symbols_table[scope]:
            self.symbols_table[scope]['variables'][id] = {'type': typE, 'value': value, 'offset': -1, 'is_global': is_global}
        else:
            self.symbols_table[scope]['variables'] = {id: {'type': typE, 'value': value, 'offset': -1, 'is_global': is_global}}
    
    def addMethod(self, scope, id, returnType, params):
        if scope not in self.symbols_table:
            self.symbols_table[scope] = {}
        if 'methods' in self.symbols_table[scope]:
            self.symbols_table[scope]['methods'][id] = {'returnType': returnType, 'params': params}
        else:
            self.symbols_table[scope]['methods'] = {id: {'returnType': returnType, 'params': params}}
    def getTable(self):
        return self.symbols_table
    
    def addOffset(self, scope, id, offset):
        if 'variables' in self.symbols_table[scope]:
            self.symbols_table[scope]['variables'][id]['offset'] = offset


    def addOffsetMethod(self, scope, funcName, id, offset):
        if not ("offset" in self.symbols_table[scope]):
            self.symbols_table[scope]["offset"] = 0
        self.symbols_table[scope]["offset"] += offset

        if 'methods' in self.symbols_table[scope]:
            self.symbols_table[scope]['methods'][funcName]['params'][id]['offset'] = offset