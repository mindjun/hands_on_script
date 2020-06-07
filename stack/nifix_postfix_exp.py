# -*- coding:utf-8 -*-

import string
from stack.linkedstack import LinkedStack


class NiPostFix(object):
    def __init__(self):
        self.stk = LinkedStack()
        self.numstl = LinkedStack()
        self.allchar = ['+', '-', '*', '/']

    def nifix_to_postfix(self, nifix):
        postfix = ''
        # for index,item in enumerate(nifix):
            # if nifix[index+1] in ','.join(string.digits):
            #     ch = item + nifix[index+1]
            #     break
            # else:
            #     ch = nifix[index]
        for ch in nifix:
            if ch in ','.join(string.digits):
                # 是数字
                if len(ch) != 1:
                    ch = ' ' + ch
                postfix += ch
            elif self.stk.isEmpty():
                # 如果这时候栈内为空，将读到的任何操作符入栈
                self.stk.push(ch)
            elif ch in ['(', '{']:
                self.stk.push(ch)
            elif ch in ['+', '-']:
                if not self.stk.isEmpty():
                    topchar = self.stk.peek()
                    while topchar in self.allchar and topchar:
                        postfix += self.stk.pop()
                        topchar = self.stk.peek() if len(self.stk) != 0 else None
                self.stk.push(ch)
            elif ch in ['*', '/']:
                if not self.stk.isEmpty():
                    topchar = self.stk.peek()
                    while topchar in ['*', '/']:
                        postfix += self.stk.pop()
                        topchar = self.stk.peek()
                self.stk.push(ch)
            elif ch in [')', '}']:
                topchar = self.stk.peek()
                while topchar not in ['(', '{']:
                    postfix += self.stk.pop()
                    topchar = self.stk.peek()
                self.stk.pop()
        topchar = self.stk.peek() if len(self.stk) != 0 else None
        while topchar:
            postfix += self.stk.pop()
            topchar = self.stk.peek() if len(self.stk) != 0 else None
        return postfix

    def calculate_postfix(self, postfix):
        for ch in postfix:
            pass

if __name__ == '__main__':
    nipostfix = NiPostFix()
    print(nipostfix.nifix_to_postfix('(51*3+7)*2-9/3'))
