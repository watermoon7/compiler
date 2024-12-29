from token_ import *
from math_ import *


# this is an old, unused class just for interpreting mathematical expressions
class Interpreter:

    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_token()
    
    def error(self, msg=None):
        if msg is not None:
            raise Exception(f"Invalid syntax: {msg}")
        raise Exception("Invalid syntax.")

    def eat(self, token_type):
        """
        Checks that the current token is of the passed type
        Throws an error if not, and gets the next token otherwise
        """
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_token()
        else:
            self.error(f"Unmatched token. Expected {token_type}, but got {self.current_token.type}")

    def factor(self):
        """ factor: INTEGER | RATIONAL | LPAREN expr RPAREN | variable """
        
        token = self.current_token
        result = None
        if token.type == INTEGER:
            self.eat(INTEGER)
            result = token.value
        elif token.type == RATIONAL:
            self.eat(RATIONAL)
            result = token.value
        elif token.type == LPAREN:
            self.eat(LPAREN)
            result = self.expr()
            self.eat(RPAREN)
        elif token.type == VARIABLE:
            self.eat(VARIABLE)
            result = token.value
        
        if result is None:
            self.error(f"Expected a INTEGER | RATIONAL or LPAREN but got {token.type} with value {token.value}")

        if self.current_token.type == FACTORIAL:
            self.eat(FACTORIAL)
            result = factorial(result)
        
        if self.current_token.type == CARET:
            self.eat(CARET)
            result = pow_(result, self.factor())

        return result
    

    def term(self):
        """ term: factor ((MUL | DIV) factor)* """
        result = self.factor()
        while (token_type := self.current_token.type) in (MUL, DIV, LPAREN, VARIABLE):
            if token_type in (MUL, LPAREN, VARIABLE):
                if token_type == MUL:
                    self.eat(MUL)
                result *= self.factor()
            elif token_type == DIV:
                self.eat(DIV)
                result /= self.factor()
                if result.is_integer():
                    result = int(result)

        return result
    
    def expr(self):
        """ expr: term ((PLUS | MINUS) term)* """
        result = self.term()
        while (token_type := self.current_token.type) in (PLUS, MINUS):
            if token_type == PLUS:
                self.eat(PLUS)
                result += self.term()
            elif token_type == MINUS:
                self.eat(MINUS)
                result -= self.term()
        
        return result

    """ Grammar
    expr   : term ((PLUS | MINUS) term)*
    term   : factor ((MUL | DIV) factor)*
    factor : INTEGER | RATIONAL | LPAREN expr RPAREN | variable
    """
