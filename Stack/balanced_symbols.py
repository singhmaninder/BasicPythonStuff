# Balanced symbols means that each opening symbol has a corresponding
# closing symbol and the pairs of symbols are properly nested.
# Following algorithm will read a string of symbols from left to right
# and decide whether the symbols are balanced.

# Import the Stack class as defined previously
from stack_implementation_second_method import Stack

def symbols_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in '([{':
            s.push(symbol)
        elif s.is_empty():
            balanced = False
        else:
            if not matches_symbols(s.pop(), symbol):
                balanced = False
        
        index += 1
        
    if balanced and s.is_empty():
        return True
    else:
        return False

def matches_symbols(opening_symbol, closing_symbol):
    opens = '([{'
    closes = ')]}'
    return opens.index(opening_symbol) == closes.index(closing_symbol)

print symbols_checker('(())')
print symbols_checker('(()))')
print symbols_checker('({)}')
print symbols_checker('({})')
print symbols_checker('{{([][])}()}')

#Output : True
# False
# False
# True
# True