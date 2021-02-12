'''
    Python program to check for
    balanced brackets.
'''
def isBalanced(string):

    stack = []
    for char in string:
        if char in ['(', '{', '[']:
            stack.append(char)

        else:

            """
            if current character is not opening
            bracket, then it must be closing.
            so stack cannot be empty at this point
            """
            if not stack:
                return False

            last_char = stack.pop()
            if last_char == '(':
                if char != ')':
                    return False

            if last_char == '{':
                if char != '}':
                    return False

            if last_char == '[':
                if char != ']':
                    return False

    # Check Empty Stack
    if stack:
        return False
    return True


if __name__ == '__main__':
    for _ in range(int(input())):
        string = input()
        res = isBalanced(string)

        if isBalanced(string):
            print('Yes')
        else:
            print("No")