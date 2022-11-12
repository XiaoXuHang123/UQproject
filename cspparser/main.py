import sys

from antlr4 import *
from antlr4.tree import ParseTreeMatch
from antlr4 import ParseTreeWalker
from antlr4 import ParseTreeVisitor
from cspParserLexer import cspParserLexer
from cspParserParser import cspParserParser
from cspParserVisitor import cspParserVisitor
input = FileStream('csp_handshake.txt')
lexer = cspParserLexer(input)
stream = CommonTokenStream(lexer)
parser = cspParserParser(stream)  # type: cspParserParser
parser.buildParseTrees = True
specification = parser.specification()
# print(specification.getText())
visitor=cspParserVisitor()
print(visitor.visit(specification))

