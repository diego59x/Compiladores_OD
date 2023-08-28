# Antlr imports
from antlr4 import InputStream, CommonTokenStream

# Generated imports
from generated.GrammarLexer import GrammarLexer
from generated.GrammarParser import GrammarParser
from generated.GrammarVisitor import GrammarVisitor

# Custom Visitor Import
from utils.CustomVisitor import CustomVisitor
import json

file_name = 'test4.cl'
file_path = f'./tests/{ file_name }'

file_content = ''
with open(file_path, 'r') as file:
    file_content = file.read()

input_stream = InputStream(file_content)
lexer = GrammarLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = GrammarParser(stream)
tree = parser.program()

visitor = CustomVisitor()
visitor.visit(tree)

symbols_table = json.dumps(visitor.getSymbolsTable(), indent=4)
errors_table = visitor.getErrorsTable()
# print(symbols_table)
if len(errors_table) > 0:
    for error in errors_table:
        print(error)
else:
    print('Success: program executed without errors.')