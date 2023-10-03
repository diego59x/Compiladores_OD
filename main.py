# Antlr imports
from antlr4 import InputStream, CommonTokenStream

# Generated imports
from generated.GrammarLexer import GrammarLexer
from generated.GrammarParser import GrammarParser
from generated.GrammarVisitor import GrammarVisitor

# Custom Visitor Import
from utils.SemanticVisitor import SemanticVisitor
from utils.IntermediateVisitor import IntermediateVisitor
import json

file_name = 'arith.cl'
file_path = f'./tests/{ file_name }'
# file_path = 'tests/arith.cl'

file_content = ''
with open(file_path, 'r') as file:
    file_content = file.read()

input_stream = InputStream(file_content)
lexer = GrammarLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = GrammarParser(stream)
tree = parser.program()

# Use semantic visitor to get symbols table and errors table    
semantic_visitor = SemanticVisitor()
semantic_visitor.visit(tree)
symbols_table = json.dumps(semantic_visitor.getSymbolsTable(), indent=4)
errors_table = semantic_visitor.getErrorsTable()
# print(symbols_table)
if len(errors_table) > 0:
    for error in errors_table:
        print(error)
else:
    print('Success: program executed without errors.')

intermediate_visitor = IntermediateVisitor()
intermediate_visitor.visit(tree)
outpupt = intermediate_visitor.getIntermediateCode()
last_class = intermediate_visitor.getCurrentClass()
if last_class is not None: outpupt += f'end_class_{last_class}\n'
with open("codigo_intermedio.txt", "w") as file:
    file.write(outpupt)
