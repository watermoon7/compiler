from token_ import EOF
from lexer import Lexer
from interpreter import Interpreter


def expr_eval():
    result = 0
    while (inp := input("math > ")) != "":
        lexer = Lexer(inp, previous_result=result)
        interpreter = Interpreter(lexer)
        result = interpreter.expr()

        if interpreter.current_token.type is not EOF:
            interpreter.error(f"Error at token {interpreter.current_token.type}")

        print(result)


if __name__ == '__main__':
    expr_eval()
