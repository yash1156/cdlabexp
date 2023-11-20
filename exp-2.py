import re

# Token types
KEYWORDS = ['int', 'float', 'if', 'else', 'while', 'for', 'return']
OPERATORS = ['[+]', '[-]', '[*]', '[/]', '[=]', '==', '!=', '<', '>', '<=', '>=']
LITERALS = r'\d+(\.\d*)?'  # Integer or floating-point literals
IDENTIFIER = r'[a-zA-Z_]\w*'  # Alphanumeric strings starting with a letter or underscore

# Regular expression for token patterns
token_patterns = [
    (re.compile(fr'\b({"|".join(KEYWORDS)})\b'), 'KEYWORD'),
    (re.compile(fr'({"|".join(OPERATORS)})'), 'OPERATOR'),
    (re.compile(fr'\b{LITERALS}\b'), 'LITERAL'),
    (re.compile(fr'\b{IDENTIFIER}\b'), 'IDENTIFIER'),
    (re.compile(r'\b(\{|\}|\(|\)|;)\b'), 'DELIMITER'),
    (re.compile(r'\s+'), 'WHITESPACE'),  # Ignore whitespace
]

def lexical_analyzer(input_code):
    tokens = []
    while input_code:
        match = None
        for pattern, token_type in token_patterns:
            match = pattern.match(input_code)
            if match:
                value = match.group(0)
                if token_type != 'WHITESPACE':
                    tokens.append((token_type, value))
                input_code = input_code[len(value):].lstrip()
                break

        if not match:
            # Handle unrecognized characters or tokens
            print(f"Error: Unrecognized token at the beginning of: {input_code[0]}")
            input_code = input_code[1:]

    return tokens

# Example usage
source_code = """
int main() {
    int x = 5;
    float y = 3.14;
    if (x > y) {
        return x;
    } else {
        return y;
    }
}
"""

tokens = lexical_analyzer(source_code)
for token in tokens:
    print(token)
