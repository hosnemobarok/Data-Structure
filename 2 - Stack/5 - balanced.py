for _ in range(int(input())):
    string = input()
    stack = ['e']

    #################append###############

    for ch in string:
        if ch == '(' or ch == '{' or ch == '[' or ch == '<':
            stack.append(ch)

        #################pop#####################

        if ch == ')':
            k = stack.pop()
            if k != '(':
                stack.append('')
                break

        elif ch == '}':
            k = stack.pop()
            if k != '{':
                stack.append('')
                break

        elif ch == ']':
            k = stack.pop()
            if k != '[':
                stack.append('')
                break

        elif ch == '>':
            k = stack.pop()

            if k != '<':
                stack.append(ch)
                break

    if stack == 0 or stack[len(stack) - 1] != 'e':
        print('NO')
    else:
        print("YES")