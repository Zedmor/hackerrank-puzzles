"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *,
/ operators and empty spaces . The integer division should truncate toward
zero.

You may assume that the given expression is always valid.

Some examples:
"3+2*2" = 7
" 3/2 " = 1
" 3+5 / 2 " = 5

"""


class Solution(object):
    def resop(self, num1, num2, operator):
        num1 = int(num1)
        num2 = int(num2)
        if operator == '+':
            return str(num1 + num2)
        if operator == '-':
            return str(num1 - num2)
        if operator == '*':
            return str(num1 * num2)
        if operator == '/':
            return str(num1 // num2)
    def orderofcomputation(self, oper1):
        if oper1[1] in '*/':
            return 0
        else:
            return 1
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        import re
        import itertools
        numbers = re.findall(r'\d+', s)
        operators = re.findall(r'\+|\-|\*|\/+', s)
        # print(numbers, operators)
        numbackup = numbers[:]
        operbackup = operators[:]
        #listorder = list(reversed(range(len(operators))))
        listorder = [(numbers[i[0]],i[1], numbers[i[0]+1]) for i in sorted(
                enumerate(
                operators),
                                          key=self.orderofcomputation)]
        listorder = list(reversed(listorder))
        subjects = []

        while listorder:
            operation = listorder.pop()
            replacement = self.resop(numbackup[operation],
                                     numbackup[operation + 1],
                                     operbackup[operation])
            # stack.append(numbackup[operation])
            # stack.append(operbackup[operation])
            # stack.append(numbers[operation+1])

            numbackup[operation] = replacement
            numbackup[operation + 1] = None
            operbackup.pop(operation)
            # for position, item in enumerate(listorder):
            #     if item > operation:
            #         listorder[position] -= 1

                    # = replacement

        return int(numbackup[0])

st = '2+3*5+1*4'
print(Solution().calculate(st))