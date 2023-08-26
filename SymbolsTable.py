class SymbolsTable:
    def __init__(self):
        self.attributes = {}
        self.methods = {}
        self.local_variables = {}
    def __str__(self):
        return "Attributes: " + str(self.attributes) + "\nMethods: " + str(self.methods) + "\nLocal Variables: " + str(self.local_variables)

    # ATTRIBUTES FUNCTIONS
    def add_attribute(self, name, value, type):
        self.attributes[name] = {'value': value, 'type': type}
    def get_attribute(self, name):
        return self.attributes.get(name, None)

    # METHODS FUNCTIONS
    def add_method(self, name, params, return_type):
        self.methods[name] = {'params': params, 'return_type': return_type}
        # self.methods[name] = information
    def get_method(self, name):
        return self.methods.get(name, None)

    # LOCAL VARIABLES FUNCTIONS
    def add_local_variable(self, name, value, scope, type):
        self.local_variables[name] = {'value': value, 'scope': scope, 'type': type}
        # self.local_variables[name] = value
    def get_local_variable(self, name):
        return self.local_variables.get(name, None)
    
    def getTable(self):
        return {'attributes': self.attributes, 'methods': self.methods, 'local_variables': self.local_variables}
