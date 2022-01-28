while True:
    value = input()
    stack = []

    if value == '.':
        break
    
    for i in value:
        if i == '(' or i == '[':
            stack.append(i)

        elif i == ']':
            if len(stack)!=0 and stack[-1] =='[':
                stack.pop()
            else:
                stack.append(']')
                break
        
        elif i == ')':
            if len(stack)!=0 and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(')')
                break
    
    if len(stack) == 0:
        print('yes')
    else:
        print('no')