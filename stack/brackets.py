
from stack.linkedstack import LinkedStack


def backetBalence(exp):
    stk = LinkedStack()
    for ch in exp:
        if ch in ['{', '(']:
            stk.push(ch)
        elif ch in ['}', ')']:
            if stk.isEmpty():
                return False
            topChar = stk.pop()
            if (ch == '}' and topChar != '{' or
                ch == ')' and topChar != '('):
                return False
    return stk.isEmpty()

result = backetBalence('{}(){}')
if result:
    print('yes')
else:
    print('no')
