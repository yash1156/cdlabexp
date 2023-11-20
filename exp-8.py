class LL1Parser:
    def __init__(self, input_str):
        self.input_str = input_str + '$'
        self.stack = ['$']
        self.first_sets = {
            'E': {'(', 'id'},
            'E\'': {'+', epsilon},
            'T': {'(', 'id'},
            'T\'': {'*', epsilon},
            'F': {'(', 'id'}
        }
        self.follow_sets = {
            'E': {')', '$'},
            'E\'': {')', '$'},
            'T': {'+', ')', '$'},
            'T\'': {'+', ')', '$'},
            'F': {'*', '+', ')', '$'}
        }
        self.table = {
            'E': {'(': 'TE\'', 'id': 'TE\''},
            'E\'': {'+': '+TE\'', ')': epsilon, '$': epsilon},
            'T': {'(': 'FT\'', 'id': 'FT\''},
            'T\'': {'+': epsilon, '*': '*FT\'', ')': epsilon, '$': epsilon},
            'F': {'(': '(E)', 'id': 'id'}
        }

    def parse(self):
        print("First Sets:")
        self.display_sets(self.first_sets)
        print("\nFollow Sets:")
        self.display_sets(self.follow_sets)
        print("\nParsing Table:")
        self.display_table(self.table)

        current_input = self.input_str[0]

        while self.stack[-1] != '$':
            current_stack_top = self.stack[-1]

            if current_stack_top in self.table and current_input in self.table[current_stack_top]:
                production = self.table[current_stack_top][current_input]
                self.stack.pop()  # Pop current stack top
                self.push_production(production)
            elif current_stack_top == current_input:
                self.stack.pop()  # Matched, pop from both stack and input
                self.consume_input()
            else:
                print("Error: Invalid input!")
                return False

        print("\nParsing successful!")
        return True

    def display_sets(self, sets):
        for non_terminal, symbols in sets.items():
            print(f"First({non_terminal}): {symbols}")

    def display_table(self, table):
        header = [''] + list(table['E'].keys())
        print("   ".join(header))
        for non_terminal, row in table.items():
            row_values = [non_terminal] + list(row.values())
            print("   ".join(row_values))

    def push_production(self, production):
        # Push the symbols of the production in reverse order
        for symbol in production[::-1]:
            if symbol != epsilon:
                self.stack.append(symbol)

    def consume_input(self):
        # Move to the next input symbol
        self.input_str = self.input_str[1:]

# Example usage:
epsilon = 'ε'
expression_input = "id + id * id"
parser = LL1Parser(expression_input)
parser.parse()
