def all_the_symbols(first: str, second: str) -> list:
    collected_symbols = []
    for current_symbol_as_int in range(ord(first)+1, ord(second), +1):
        collected_symbols.append(chr(current_symbol_as_int))
    return collected_symbols


char1 = input()
char2 = input()
symbols = all_the_symbols(char1, char2)
print(" ".join(symbols))