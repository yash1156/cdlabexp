class LALRParser:
    grammar_rules = [
        "S -> E",
        "E -> E + T",
        "E -> T",
        "T -> T * F",
        "F -> ( E )",
        "F -> id"
    ]

    item_sets = {}

    def __init__(self):
        self.initialize_item_sets()

    def display_item_sets(self):
        print("Item Sets : ")
        for non_terminal, items in self.item_sets.items():
            print(f"{non_terminal} : {items}")

    def initialize_item_sets(self):
        for rule in self.grammar_rules:
            parts = rule.split("->")
            non_terminal = parts[0].strip()
            production = parts[1].strip()
            items = set()

            for i in range(len(production) + 1):
                items.add(production[:i] + " . "+ production[i:])

            self.item_sets[non_terminal] = items

if __name__ == "__main__":
    parser = LALRParser()
    parser.display_item_sets()        