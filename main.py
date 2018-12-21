import sys
from antlr4 import *
from CLexer import CLexer
from CParser import CParser


def main(argv):
    input = FileStream('test.c' if len(argv) <= 1 else argv[1])
    lexer = CLexer(input)
    stream = CommonTokenStream(lexer)
    parser = CParser(stream)
    tree = parser.compilationUnit()
    print(tree.toStringTree(recog=parser))


if __name__ == '__main__':
    main(sys.argv)