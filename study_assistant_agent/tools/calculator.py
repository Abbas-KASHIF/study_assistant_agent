import ast
import operator as op
from typing import Union


Number = Union[int, float]

_ALLOWED_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.USub: op.neg,
    ast.UAdd: op.pos,
    ast.Mod: op.mod,
}


def safe_calculate(expression: str) -> Number:
    """
    Safely evaluate a basic arithmetic expression without using eval().

    Supported operations: +, -, *, /, **, %, parentheses and unary +/-.
    """
    if not expression or not expression.strip():
        raise ValueError("Expression cannot be empty.")

    tree = ast.parse(expression, mode="eval")
    return _eval_node(tree.body)


def _eval_node(node: ast.AST) -> Number:
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in _ALLOWED_OPERATORS:
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        return _ALLOWED_OPERATORS[type(node.op)](left, right)

    if isinstance(node, ast.UnaryOp) and type(node.op) in _ALLOWED_OPERATORS:
        return _ALLOWED_OPERATORS[type(node.op)](_eval_node(node.operand))

    raise ValueError("Unsupported or unsafe expression.")
