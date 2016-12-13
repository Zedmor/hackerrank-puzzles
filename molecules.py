def equals_atomically (obj1, obj2):
    if len(obj1) != len(obj2):
        return False
    for k in obj1:
        if obj1[k] != obj2[k]:
            return False
    return True


from collections import Counter
import re

COMPONENT_RE = (
    r'('
    r'[A-Z][a-z]?'
    r'|'
    r'\([^(]+\)'
    r'|'
    r'\[[^[]+\]'
    r'|'
    r'\{[^}]+\}'
    r')'
    r'(\d*)'
)

def parse_molecule(formula):
    counts = Counter()
    for element, count in re.findall(COMPONENT_RE, formula):
        count = int(count) if count else 1
        if element[0] in '([{':
            for k, v in parse_molecule(element[1:-1]).items():
                counts[k] += count * v
        else:
            counts[element] += count
    return counts
    # import re
    # from functools import reduce
    # import operator
    #
    # def repint(s):
    #     try:
    #         int(s)
    #         return True
    #     except (ValueError, TypeError) as e:
    #         return False
    #
    # def prod(iterable):
    #     return reduce(operator.mul, iterable, 1)
    # def processlst(lst, stack):
    #         while lst:
    #             lst = list(filter(None, lst))
    #             if len(lst) is 1:
    #                 if isinstance(lst[0], list):
    #                     lst = lst[0]
    #             last = lst.pop()
    #             if isinstance(last, list):
    #                 processlst(last,stack)
    #                 if stack:
    #                     stack.pop()
    #             else:
    #                 if repint(last):
    #                     if lst:
    #                         if isinstance(lst[-1], list):
    #                             stack.append(int(last))
    #                 else:
    #                     # print('str!',prod(stack), last)
    #                     finstr = list(filter(None, re.split(r'(\D+)(\d+)',last)))
    #                     numfst = list(filter(None, re.split(r'(\d+)(\D+)',last)))
    #                     if len(finstr)==2:
    #                         splitted = re.findall(r'[A-Z][^A-Z]*', finstr[0])
    #                         value = int(finstr[-1])
    #                         if stack:
    #                             value *= prod(stack)
    #                         try:
    #                             finaldict[splitted[-1]]+=value
    #                         except KeyError:
    #                             finaldict[splitted[-1]] = value
    #                         for i in splitted[:-1]:
    #                             try:
    #                                 finaldict[i] += prod(stack)
    #                             except KeyError:
    #                                 finaldict[i] = prod(stack)
    #                     elif len(finstr)==1 and len(numfst)<2:
    #                         splitted = re.findall(r'[A-Z][^A-Z]*', finstr[0])
    #                         for i in splitted:
    #                             try:
    #                                 finaldict[i] +=prod(stack)
    #                             except KeyError:
    #                                 finaldict[i] = prod(stack)
    #                     else:
    #                         splitted = re.findall(r'[A-Z][^A-Z]*', last)
    #                         if repint(finstr[0]):
    #                             lst.append(finstr[0])
    #                         if repint(numfst[0]):
    #                             lst.append(numfst[0])
    #                             # splitted = finstr[:1] + splitted
    #                         for i in splitted:
    #                             processlst([i],stack)
    #
    #         #     if lst[-2] is lst:
    #         #         lst = lst[:-2]+[[last, z] for z in lst[-2]]
    #         #     print(lst)
    #         #
    #         # else:
    #         #     return lst
    #
    # formula = re.sub(r"[(\[{]", "',['", formula)
    # formula = re.sub("[)}\]]", "'],'", formula)
    # formula = "['" + formula + "']"
    # # print(formula)
    # d = eval(formula)
    # finaldict = {}
    # processlst(list(filter(None,d)), [])
    # return finaldict
    # # print(numbers)



# print(parse_molecule("K4[ON(SO3)2]2"))

print(parse_molecule("{[Co(NH3)4(OH)2]3Co}(SO4)3"))

