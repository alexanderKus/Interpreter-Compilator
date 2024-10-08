from enum import Enum


class TokenKind(Enum):
    # Single-character tokens.
    LEFT_PAREN = 0,
    RIGHT_PAREN = 1,
    LEFT_BRACE = 2,
    RIGHT_BRACE = 3,
    COMMA = 4,
    DOT = 5,
    MINUS = 6,
    PLUS = 7,
    SEMICOLON = 8,
    SLASH = 9,
    STAR = 10,

    # One or two character tokens.
    BANG = 11,
    BANG_EQUAL = 12,
    EQUAL = 13,
    EQUAL_EQUAL = 14,
    GREATER = 15,
    GREATER_EQUAL = 16,
    LESS = 17
    LESS_EQUAL = 18,

    # Literals.
    IDENTIFIER = 19,
    STRING = 20,
    NUMBER = 21

    # Keywords.
    AND = 22,
    CLASS = 23,
    ELSE = 24,
    FALSE = 25,
    FUN = 26,
    FOR = 27,
    IF = 28,
    NIL = 29,
    OR = 30,
    PRINT = 31,
    RETURN = 32,
    SUPER = 33,
    THIS = 34,
    TRUE = 35
    VAR = 36,
    WHILE = 37,
    BREAK = 38

    EOF = 39

class Token:
    def __init__(self, kind, lexeme, literal, line):
        self.kind = kind
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def _str__(self):
        return f'TOKEN: {self.kind} {self.lexeme} {self.literal}'
