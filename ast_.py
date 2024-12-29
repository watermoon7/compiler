# class definitions of nodes and leaves for the ast

class BinOp:
    
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __str__(self):
        return f"BinOP(\n\tleft={self.left}\n\top={self.op}\n\tright={self.right}\n)"

    def __repr__(self):
        return self.__str__()


class UnaryOp:
    
    def __init__(self, op, expr):
        self.token = self.op = op
        self.expr = expr

    def __str__(self):
        return f"{self.op}{self.expr}"

    def __repr__(self):
        return self.__str__()


class Num:
    
    def __init__(self, token):
        #self.token = token
        self.value = token.value

    def __str__(self):
        return f"Num({self.value})"

    def __repr__(self):
        return self.__str__()
