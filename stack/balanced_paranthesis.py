def isBalanced(s):
    stack =[]
    s = [i for i in s]
    rev = {
        '}':'{',
        ']':'[',
        ')':'('
    }
    pass
    while s:
        if s[0] in ['(', '{', '[']:
            stack.append(s.pop(0))
        else:
            try:
                a = stack.pop(-1)
                b = s.pop(0)
                if a != rev[b]: break
            except:
                break
    return 'NO' if s else 'YES'


if __name__ == '__main__':
    data = [

        '([[)'
    ]

    [print(i, isBalanced(i)) for i in data]
