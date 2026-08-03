def isvalidParen(value):
    matching = {
        "(" : ")",
        "[" : "]",
        "{" : "}"
    }

    stack = []

    for char in value:
        if char in "([{":
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            top_value = stack[-1]
            if matching[top_value] == char:
                stack.pop()
            else:
                return False
    
    if len(stack) == 0:
        return True
    return False        



print(isvalidParen("()[]{}"))   # expected True
print(isvalidParen("(]"))        # expected False
print(isvalidParen("([)]"))      # expected False
print(isvalidParen("{[]}"))      # expected True
print(isvalidParen("(])"))       # expected False (unclosed)

