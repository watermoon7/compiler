PERIOD, EOF = 'PERIOD', 'EOF'
INTEGER, RATIONAL = 'INTEGER', 'RATIONAL'

PLUS, MINUS, MUL, DIV = 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE'
LPAREN, RPAREN = 'LPAREN', 'RPAREN'
FACTORIAL, CARET = 'FACTORIAL', 'CARET'

VARIABLE = 'VARIABLE'

class Token():
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __str__(self):
        return f'Token({self.type}, {self.value})'

    def __repr__(self):
        return self.__str__()
