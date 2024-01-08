class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def insert(self, name, symbol_type):
        if name not in self.symbols:
            self.symbols[name] = symbol_type
            return True
        else:
            return False  # Symbol already exists

    def lookup(self, name):
        return self.symbols.get(name, None)

    def display(self):
        print("Symbol Table:")
        for name, symbol_type in self.symbols.items():
            print(f"{name}: {symbol_type}")

# Example usage:
symbol_table = SymbolTable()

symbol_table.insert("x", "int")
symbol_table.insert("y", "float")
symbol_table.insert("x", "string")  # This will return False, as "x" already exists

print("Type of x:", symbol_table.lookup("x"))  # Output: int
print("Type of z:", symbol_table.lookup("z"))  # Output: None

symbol_table.display()
