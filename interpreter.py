from token_ import *
from math_ import *


class NodeVisitor(object):
    
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f"No visit_{type(node).__name__} method exists.")
    

class Interpreter(NodeVisitor):

    def __init__(self, parser):
        self.parser = parser

    def visit_BinOp(self, node):
        op = node.op.type
        if op == PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif op == MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif op == MUL:
            return self.visit(node.left) * self.visit(node.right)
        elif op == DIV:
            return self.visit(node.left) / self.visit(node.right)
        elif op == CARET:
            return pow_(self.visit(node.left), self.visit(node.right))
        
    def visit_UnaryOp(self, node):
        op = node.op.type
        if op == PLUS:
            return +self.visit(node.expr)
        elif op == MINUS:
            return -self.visit(node.expr)
        elif op == FACTORIAL:
            return factorial(self.visit(node.expr))
    
    def visit_Num(self, node):
        return node.value
    
    def interpret(self):
        tree = self.parser.parse()
        return self.visit(tree)
