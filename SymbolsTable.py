class SymbolsTable:
    def __init__(self):
        self.attributes = {}
        self.methods = {}
        self.local_variables = {}

    # ATTRIBUTES METHODS
    def add_attribute(self, name, value, type):
        self.attributes[name] = value
    def get_attribute(self, name):
        return self.attributes.get(name, None)

    # METHODS METHODS
    def add_method(self, name, params, return_type):
        pass
        # self.methods[name] = information
    def get_method(self, name):
        return self.methods.get(name, None)

    # LOCAL VARIABLES METHODS
    def add_local_variable(self, name, value, scope, type):
        self.local_variables[name] = value
    def get_local_variable(self, name):
        return self.local_variables.get(name, None)
