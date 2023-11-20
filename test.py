class PredictiveParser:
    def __init__(self, input_str):
        self.input_str = input_str
        self.index = 0

    def match(self, expected_token):
        if self.index < len(self.input_str) and self.input_str[self.index] == expected_token:
            self.index += 1
        else:
            raise Exception(f"Error: Expected {expected_token}, found {self.input_str[self.index]}")

    def E(self):
        self.T()
        self.E_prime()

    def E_prime(self):
        if self.index < len(self.input_str) and self.input_str[self.index] == '+':
            self.match('+')
            self.T()
            self.E_prime()

    def T(self):
        self.F()
        self.T_prime()

    def T_prime(self):
        if self.index < len(self.input_str) and self.input_str[self.index] == '*':
            self.match('*')
            self.F()
            self.T_prime()

    def F(self):
     if self.index < len(self.input_str) and self.input_str[self.index] == '(':
        self.match('(')
        self.E()
        self.match(')')
     elif self.index < len(self.input_str) and self.input_str[self.index].isalpha():
        while self.index < len(self.input_str) and (self.input_str[self.index].isalpha() or self.input_str[self.index].isdigit()):
            self.index += 1
     else:
        raise Exception("Error: Invalid expression")


    def parse(self):
     try:
        self.E()
        if self.index == len(self.input_str):
            print("Parsing successful.")
        else:
            raise Exception(f"Error: Incomplete expression at position {self.index}")
     except Exception as e:
        print(e)


# Example usage
input_expression = "id + id * id"
parser = PredictiveParser(input_expression)
parser.parse()
