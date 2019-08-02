"""
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
>>> Solution().fullJustify(["What","must","be","acknowledgment","shall","be"], 16)
['What   must   be', 'acknowledgment  ', 'shall be        ']

Input:
>>> Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
['This    is    an', 'example  of text', 'justification.  ']

Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""
from itertools import zip_longest


def add_space(spaces_slots):
    pointer = 0
    while True:
        for i in range(len(spaces_slots)):
            spaces_slots[i] += ' '
            yield spaces_slots


def total_len(line, spaces_slots):
    return len(''.join(line) + ''.join(spaces_slots))


def format_result(result, maxWidth):
    new_result = []
    for i, line in enumerate(result):
        spaces_slots = [''] * (len(line) - 1)
        if not spaces_slots:
            spaces_slots = ['']
        adder = add_space(spaces_slots)
        while total_len(line, spaces_slots) < maxWidth:
            spaces_slots = next(adder)
        if i == len(result) - 1:
            new_line = ' '.join(line)
            new_line += ' ' * (maxWidth - len(new_line))
        else:
            new_line = ''.join(['{}{}'.format(a, b) for a, b in zip_longest(line, spaces_slots, fillvalue='')])
        new_result.append(new_line)

    return new_result




class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        while words:
            line_len = 0
            line = []
            while words:
                word = words.pop(0)

                line.append(word)
                line_len = line_len + len(word) + 1 # For space

                if line_len > maxWidth + 1:
                    line.pop(-1)
                    words = [word] + words
                    break

            result.append(line)

        result = format_result(result, maxWidth)

        return result
