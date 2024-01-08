class RecursiveDescentParser:
    def __init__(self, input_string):
        self.tokens = self.tokenize(input_string)
        self.current_token = 0

    def tokenize(self, input_string):
        # Simple lexer that tokenizes the input string into numbers, operators, and parentheses
        # You might want to use a more sophisticated lexer for a real-world application.
        return input_string.replace(' ', '').split('+')  # Replace with a proper lexer

    def parse(self):
        return self.parse_expression()

    def parse_expression(self):
        result = self.parse_term()
        while self.current_token < len(self.tokens) and self.tokens[self.current_token] in ('+', '-'):
            op = self.tokens[self.current_token]
            self.current_token += 1
            right = self.parse_term()
            if op == '+':
                result += right
            elif op == '-':
                result -= right
        return result

    def parse_term(self):
        result = self.parse_factor()
        while self.current_token < len(self.tokens) and self.tokens[self.current_token] in ('*', '/'):
            op = self.tokens[self.current_token]
            self.current_token += 1
            right = self.parse_factor()
            if op == '*':
                result *= right
            elif op == '/':
                result /= right
        return result

    def parse_factor(self):
        if self.tokens[self.current_token] == '(':
            self.current_token += 1
            result = self.parse_expression()
            if self.tokens[self.current_token] == ')':
                self.current_token += 1
                return result
            else:
                raise SyntaxError("Expected closing parenthesis")
        else:
            result = int(self.tokens[self.current_token])
            self.current_token += 1
            return result

# Example usage:
input_string = "3 + 5 * ( 4 - 2 )"
parser = RecursiveDescentParser(input_string)
result = parser.parse()
print(f"Result: {result}")
