class SymbolsTable:
    def __init__(self):
        self.symbols_table = {}
    def addScope(self, scope):
        if scope not in self.symbols_table:
            self.symbols_table[scope] = {}
    def addInherits(self, scope, inherits):
        self.symbols_table[scope]['inherits'] = inherits
    def addVariable(self, scope, id, typE, value):
        if 'variables' in self.symbols_table[scope]:
            self.symbols_table[scope]['variables'][id] = {'type': typE, 'value': value}
        else:
            self.symbols_table[scope]['variables'] = {id: {'type': typE, 'value': value}}
    def addMethod(self, scope, id, returnType, params):
        if scope not in self.symbols_table:
            self.symbols_table[scope] = {}
        self.symbols_table[scope]['methods'] = {id: {'returnType': returnType, 'params': params}}
    def getTable(self):
        return self.symbols_table