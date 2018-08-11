"""
Problem Statement
You are given an integer (provided as s as it may be up to 50 digits in length). Return the number of subsequences of digits in the number that themselves compose an integer that is divisible by 3. Since this count could be very large, return the number mod 1000000007.

Definition
Class: MagicNumberThree
Method: countSubsequences
Parameters: string
Returns: integer
Method signature: def countSubsequences(self, s):
Limits
Time limit (s): 2.000
Memory limit (MB): 256
Constraints
- s will contain between 1 and 50 characters, inclusive.
- Each character of s will be between '0' and '9', inclusive.
Examples
0)
"132"
Returns: 3
There are 7 total subsequences of the given digits, but only some of them work: 3, 12, and 132 are divisible by 3. 1, 2, 13, and 32 are not.
1)
"9"
Returns: 1
There's only one subsequence to consider here, and it is divisible by 3.
2)
"333"
Returns: 7
There are three ways to make a "3" as a subsequence, and we could all of them individually. There are also three ways to make a subsequence of "33", which we also count. And, of course, "333" also works.
3)
"123456"
Returns: 23
4)
"00"
Returns: 3
Remember that 0 is divisible by three. The sequence 00 of course also has the value 0.
This problem statement is the exclusive and proprietary property of TopCoder, Inc. Any unauthorized use or reproduction of this information without the prior written consent of TopCoder, Inc. is strictly prohibited. (c)2003, TopCoder, Inc. All rights reserved.

"""

class MagicNumberThree:
    def countSubsequences(self, s):

        return 0
