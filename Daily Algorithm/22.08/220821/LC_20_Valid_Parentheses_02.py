
s = "()"

def isValid(s):

    stack = [0]
    matches = {0: None, '{': '}', '[': ']', '(': ')'}

    for paren in s:
        if paren in matches:
            stack.append(paren)

        else:
            if matches[stack.pop()] != paren:
                return False

    return stack == [0]


print(isValid(s))

