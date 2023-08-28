class ErrorTable():
    def __init__(self):
        self.errors = []
    def getErrors(self):
        return self.errors
    def addScopeError(self, line, varName):
        error = f'Error in line { line }: { varName } is not defined in the current scope.'
        self.errors.append(error)
    def addAssignationError(self, line, varName, expectedVarType, receivedVarType):
        error = f'Error in line { line }: { varName } expected { expectedVarType } but { receivedVarType } was given.'
        self.errors.append(error)
    def addParameterCountError(self, line, funcName, numParams):
        error = f'Error in line {line}: { funcName } expected { numParams } parameters.'
        self.errors.append(error)
    def addParameterTypeError(self, line, funcName, paramType, expectedType):
        error = f'Error in line {line}: { funcName } expected { expectedType } parameter but { paramType } was given.'
        self.errors.append(error)
    def addVariableTypeError(self, line, recievedType):
        error = f'Error in line {line}: { recievedType } is not a valid type.'
        self.errors.append(error)
    def addVariableDeclarationTypeError(self, line, varName, expectedType, receivedType):
        error = f'Error in line {line}: { varName } expected { expectedType } but { receivedType } was given.'
        self.errors.append(error)
    def addStringQuotesError(self, line):
        error = f'Error in line {line}: String must be between double quotes.'
        self.errors.append(error)
    def addOperationError(self, line, operationType, leftType, rightType):
        error = f'Error in line {line}: { operationType } is not a valid operation for { leftType } and { rightType }.'
        self.errors.append(error)
    def addMainShouldInheritIOError(self, line):
        error = f'Error in line {line}: Main should inherit IO.'
        self.errors.append(error)
    def addVarAlreadyExistsError(self, line, varName):
        error = f'Error in line {line}: { varName } already exists in the current scope.'
        self.errors.append(error)
    
    