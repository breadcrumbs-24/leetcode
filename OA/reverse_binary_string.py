"""
You are given a binary string. Find the minimum number of operations required to reverse it.
An operation is defined as: Remove a character from any index and append it to the end of the string-

EG:
S = "00110101"
00110101 - 00101011 (Index 3 appended to the end)
00101011 - 01010110 (Index 0 appended to the end)
01010110 - 10101100 (Index 0 appended to the end)

So the answer is 3 opertations

Constraints
1 < S.length <= 1e5
"""

"""
Goal: Find the minimum number of operations required to turn S into reverse(S)
Operation: Remove a character at any index and append it to the end of the string

S = Original String
T = reversed String
We want to make S T with the least interaction

Steps:
1. S = T[::-1]
2. Try to align the sufix of S with the prefix of T
3. Find the longest sufix of S that matches the prefix of T
4. The min number of operations required = len(S) - longest_match



S = "00110101"
T = "10101100"
"""

00110101