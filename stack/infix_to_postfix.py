def infix_to_postfix(expr):
    stack = []
    postfix = []

    prec = {
        '+': 1,
        '-': 1,
        '/': 2,
        '*': 2,
        '^': 3
    }

    for char in expr:
        if char.isalpha(): postfix.append(char)
        if char == '(': stack.append(char)

        if char == ')':
            while True:
                operator = stack.pop(-1)
                if operator == '(': break
                else:
                    postfix.append(operator)

        if char in prec.keys():
            while stack and stack[-1] in prec.keys() and prec[char] <= prec[stack[-1]]:
                postfix.append(stack.pop(-1))
            stack.append(char)

    
    if stack:
        postfix.append(stack.pop(-1))

    return ''.join( postfix)

if __name__ == '__main__':
    
    data = [
        'a+b',
        '(a+b/c*(d+e)-f)',
        'a+b+c+d',
        'a*b+c*d'
    ]

    res = {k: infix_to_postfix(k) for k in data}
    [print(k,v) for k,v in res.items()]