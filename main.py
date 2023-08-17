from antlr4 import InputStream, CommonTokenStream
from yapl.grammar.HelloLexer import HelloLexer
from yapl.grammar.HelloParser import HelloParser
from yapl.grammar.HelloVisitor import HelloVisitor

from CustomVisitor import *

file_path = './example.txt'
file_content = ''
# Open the file in read mode ('r')
with open(file_path, 'r') as file:
    file_content = file.read()

# Input string to parse
input_string = file_content

# Create an InputStream from the input string
input_stream = InputStream(input_string)

# Create a lexer that feeds off the input stream
lexer = HelloLexer(input_stream)
    
# Create a buffer of tokens pulled from the lexer
token_stream = CommonTokenStream(lexer)

# Create the parser with the token stream
parser = HelloParser(token_stream)

# Start parsing from the top-level rule of your grammar
tree = parser.program()

# Now you have the parse tree, and you can traverse it as needed
# For example, you can use the built-in visitor or listener classes from ANTLR

# Instantiate the visitor and visit the parse tree
visitor = CustomVisitor()
result = visitor.visit(tree)