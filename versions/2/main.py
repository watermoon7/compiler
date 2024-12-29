from lexer import Lexer
from parser import Parser
from interpreter import Interpreter


def interpret():
    result = 0
    while (inp := input("interpreter > ")) != "":
        lexer = Lexer(inp)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)

        result = interpreter.interpret()
        print(result)       


if __name__ == '__main__':
    interpret()
