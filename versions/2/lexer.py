from token_ import *
from math import pi, e

class Lexer:
    def __init__(self, code, previous_result=0):
        self.text = code
        self.previous_result=previous_result
        self.length = len(self.text)
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self, msg=None):
        if msg is not None:
            raise Exception(f"Error parsing input: {msg}")
        raise Exception("Error parsing input.")
    
    def advance(self):
        self.pos += 1
        if self.pos > self.length - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def peek(self):
        if self.pos + 1 > self.length - 1:
            return None
        else:
            return self.text[self.pos + 1]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance() 

    def number(self):
        result = ''
        decimal = False
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
            if self.current_char == '.':
                if not decimal:
                    decimal = True
                    result += '.'
                    self.advance()
                else:
                    self.error("Cannot have multiple decimal points.")

        if decimal: 
            return Token(RATIONAL, float(result))
        else:
            return Token(INTEGER, int(result))

    def variable(self):
        result = self.current_char
        self.advance()
        
        if result + str(self.current_char) == 'pi':
            result = 'pi'
            self.advance()
        elif result + str(self.current_char) + str(self.peek()) == 'ans':
            result = 'ans'
            self.advance()
            self.advance()

        match result:
            case 'pi':
                return Token(VARIABLE, pi)
            case 'e':
                return Token(VARIABLE, e)
            case 'ans':
                return Token(VARIABLE, self.previous_result)
            case _:
                return Token(VARIABLE, result)
            
    def get_token(self):
        
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return self.number()
            
            if self.current_char.isalpha():
                return self.variable()

            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')
            
            if self.current_char == '*':
                self.advance()
                return Token(MUL, '*')
            
            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')
            
            if self.current_char == '(':
                self.advance()
                return Token(LPAREN, '(')
            
            if self.current_char == ')':
                self.advance()
                return Token(RPAREN, ')')
            
            if self.current_char == '^':
                self.advance()
                return Token(CARET, '^')
            
            if self.current_char == '!':
                self.advance()
                return Token(FACTORIAL, '!')
            
            self.error(f"Unrecognised character {self.current_char}")

        return Token(EOF, None)
