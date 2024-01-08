import re

class Token:
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0

    def ignore_whitespace(self):
        while self.position < len(self.source_code) and self.source_code[self.position].isspace():
            self.position += 1

    def get_next_token(self):
        self.ignore_whitespace()

        if self.position >= len(self.source_code):
            return Token("EOF", None)

        # Keywords
        keywords = ["if", "else", "while", "var", "print"]
        for keyword in keywords:
            if self.source_code.startswith(keyword, self.position):
                self.position += len(keyword)
                return Token("KEYWORD", keyword)

        # Operators
        operators = ["+", "-", "*", "/", "=", "==", "<", ">", "<=", ">=", "!="]
        for operator in operators:
            if self.source_code.startswith(operator, self.position):
                self.position += len(operator)
                return Token("OPERATOR", operator)

        # Identifiers
        identifier_regex = r'[a-zA-Z_][a-zA-Z0-9_]*'
        match = re.match(identifier_regex, self.source_code[self.position:])
        if match:
            identifier = match.group()
            self.position += len(identifier)
            return Token("IDENTIFIER", identifier)

        # Integers
        integer_regex = r'\d+'
        match = re.match(integer_regex, self.source_code[self.position:])
        if match:
            integer_value = int(match.group())
            self.position += len(match.group())
            return Token("INTEGER", integer_value)

        # String literals
        if self.source_code[self.position] == '"':
            end_quote = self.source_code.find('"', self.position + 1)
            if end_quote != -1:
                string_literal = self.source_code[self.position + 1:end_quote]
                self.position = end_quote + 1
                return Token("STRING", string_literal)
            else:
                raise Exception("Unterminated string literal")

        # Comments
        if self.source_code.startswith("//", self.position):
            end_of_line = self.source_code.find('\n', self.position)
            if end_of_line != -1:
                self.position = end_of_line
                return self.get_next_token()
            else:
                return Token("EOF", None)

        # If no token matched, raise an exception or handle the error accordingly
        raise Exception(f"Invalid token at position {self.position}")

# Example usage:
source_code = """
    var x = 10;
    if (x > 5) {
        print("Hello, world!");
    }
    // This is a comment
"""

lexer = Lexer(source_code)

while True:
    token = lexer.get_next_token()
    if token.type == "EOF":
        break
    print(f"Token Type: {token.type}, Value: {token.value}")
