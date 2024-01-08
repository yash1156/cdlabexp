def calculate_first(grammar):
    first = {}

    # Initialize First sets for all non-terminals
    for non_terminal, _ in grammar:
        first[non_terminal] = set()

    while True:
        updated = False

        for production in grammar:
            non_terminal = production[0]
            rhs = production[1:]

            for symbol in rhs:
                if symbol.islower() or symbol == 'ε':
                    if symbol not in first[non_terminal]:
                        first[non_terminal].add(symbol)
                        updated = True
                    break
                elif symbol.isupper():
                    first[non_terminal] = first[non_terminal].union(first[symbol])
                    if 'ε' not in first[symbol]:
                        break

        if not updated:
            break

    return first


def calculate_follow(grammar, first):
    follow = {non_terminal: set() for non_terminal, _ in grammar}
    follow[grammar[0][0]].add('$')  # Add $ to the follow set of the start symbol

    while True:
        updated = False

        for production in grammar:
            non_terminal = production[0]
            rhs = production[1:]

            for i in range(len(rhs)):
                if rhs[i].isupper():
                    if i == len(rhs) - 1:
                        follow[non_terminal] = follow[non_terminal].union(follow[rhs[i]])
                    else:
                        first_of_next = first[rhs[i + 1]]
                        follow[non_terminal] = follow[non_terminal].union(first_of_next - {'ε'})
                        if 'ε' in first_of_next:
                            follow[non_terminal] = follow[non_terminal].union(follow[rhs[i]])
                            if 'ε' in follow[rhs[i]]:
                                follow[non_terminal] = follow[non_terminal] - {'ε'}

        if not updated:
            break

    return follow


# Example Grammar
grammar = [
    ('S', 'A'),
    ('A', 'a'),
    ('A', 'ε'),
]

first_set = calculate_first(grammar)
follow_set = calculate_follow(grammar, first_set)

print("First Set:")
for non_terminal, first in first_set.items():
    print(f"First({non_terminal}): {first}")

print("\nFollow Set:")
for non_terminal, follow in follow_set.items():
    print(f"Follow({non_terminal}): {follow}")
