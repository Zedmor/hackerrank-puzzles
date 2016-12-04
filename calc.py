class Calculator(object):
    def evaluate(self, string):
        import re
        nums = list(map(float,re.findall(r'[\d.]+', string)))
        operands = re.findall(r'[+\-*\/]',string)
        # print(nums,operands)
        z = 0
        for i,oper in enumerate(operands):
            if oper is '*':
                nums[i+z] *= nums[i+1+z]
                nums.pop(i+z+1)
                operands[i] = 'x'
                z -= 1
            if oper is '/':
                nums[i+z] /= nums[i + 1 + z]
                nums.pop(i+z + 1)
                operands[i] = 'x'
                z -= 1
        result = nums[0]
        operands = list(filter(('x').__ne__, operands))
        for i,oper in enumerate(operands):
            if oper is '+':
                result += nums[i+1]
            if oper is '-':
                result -= nums[i + 1]

        return result


print(Calculator().evaluate("1.1 + 2.2 + 3.3"))  # => 7