from token_ import *
from ast_ import *


class Parser:

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
        """ factor: (PLUS | MINUS) FACTOR | INTEGER | RATIONAL | LPAREN expr RPAREN  """
        
        token = self.current_token
        if token.type == PLUS:
            self.eat(PLUS)
            node = UnaryOp(token, self.factor())
        elif token.type == MINUS:
            self.eat(MINUS)
            node = UnaryOp(token, self.factor())
        elif token.type == INTEGER:
            self.eat(INTEGER)
            node = Num(token)
        elif token.type == RATIONAL:
            self.eat(RATIONAL)
            node = Num(token)
        elif token.type == VARIABLE:
            self.eat(VARIABLE)
            node = Num(token)
        elif token.type == LPAREN:
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)
        
        while (token := self.current_token).type == FACTORIAL:
            self.eat(FACTORIAL)
            node = UnaryOp(token, node)
        
        token = self.current_token
        if token.type == CARET:
            self.eat(CARET)
            node = BinOp(node, token, self.factor())
        
        return node


    def term(self):
        """ term: factor ((MUL | DIV) factor)* """
        node = self.factor()
        while (token := self.current_token).type in (MUL, DIV):
            if token.type == MUL:
                self.eat(MUL)
            else:
                self.eat(DIV)

            node = BinOp(
                left=node,
                op=token,
                right=self.factor()
            )

        return node
    
    def expr(self):
        """ expr: term ((PLUS | MINUS) term)* """
        node = self.term()
        while (token := self.current_token).type in (PLUS, MINUS):
            if token.type == PLUS:
                self.eat(PLUS)
            else:
                self.eat(MINUS)

            node = BinOp(
                left=node,
                op=token,
                right=self.term()
            )

        return node

    def parse(self):
        return self.expr()


if __name__ == '__main__':
    from lexer import *
    import jsonpickle # make a venv and install jsonpickle
    import json

    lexer = Lexer('1+2*3*(4+5)')
    parser = Parser(lexer)

    result = parser.parse()
    serialised = jsonpickle.encode(result)

    print(json.dumps(json.loads(serialised), indent=4))
