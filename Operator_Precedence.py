class Token:
    def __init__(self, token_type, value=None):
        self.token_type = token_type
        self.value = value

    def __str__(self):
        return f"({self.token_type}, {self.value})"


def tokenize(expression):
    tokens = []
    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            j = i
            while j < len(expression) and (expression[j].isdigit() or expression[j] == '.'):
                j += 1
            tokens.append(Token('NUMBER', float(expression[i:j])))
            i = j
        elif expression[i] in "+-*/()":
            tokens.append(Token(expression[i]))
            i += 1
        elif expression[i].isspace():
            i += 1
        else:
            raise ValueError(f"Invalid character: {expression[i]}")
    return tokens


def parse_expression(expression):
    tokens = tokenize(expression)
    stack = []
    output = []

    for token in tokens:
        if token.token_type == 'NUMBER':
            output.append(token)
        elif token.token_type == '(':
            stack.append(token)
        elif token.token_type == ')':
            while stack and stack[-1].token_type != '(':
                output.append(stack.pop())
            stack.pop()  # Pop the '('
        else:
            while stack and stack[-1].token_type in precedence and precedence[stack[-1].token_type] >= precedence[token.token_type]:
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output


def build_expression_tree(postfix_expression):
    stack = []

    for token in postfix_expression:
        if token.token_type == 'NUMBER':
            stack.append(token)
        elif token.token_type in precedence:
            right_operand = stack.pop()
            left_operand = stack.pop()
            stack.append(Token('EXPR', value=(token.token_type, left_operand, right_operand)))

    return stack.pop()


def evaluate_expression_tree(node):
    if node.token_type == 'NUMBER':
        return node.value
    elif node.token_type == 'EXPR':
        operator, left, right = node.value
        if operator == '+':
            return evaluate_expression_tree(left) + evaluate_expression_tree(right)
        elif operator == '-':
            return evaluate_expression_tree(left) - evaluate_expression_tree(right)
        elif operator == '*':
            return evaluate_expression_tree(left) * evaluate_expression_tree(right)
        elif operator == '/':
            return evaluate_expression_tree(left) / evaluate_expression_tree(right)
        else:
            raise ValueError(f"Invalid operator: {operator}")


precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
}

def main():
    expression = input("Enter an arithmetic expression: ")
    postfix_expression = parse_expression(expression)
    expression_tree = build_expression_tree(postfix_expression)
    result = evaluate_expression_tree(expression_tree)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
