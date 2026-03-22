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

"""
What I can keep on place?
Every operation removes one character and move it to the end the remaining characters matter
operations = len(S) - longestMatch
"""

def min_operations_to_reverse(S):
    # Esto se usa para revertir el array
    T = S[::-1]
    # ponemos la longitud de S
    n = len(S)
    
    # Apuntamos a 0
    j = 0 # pointer for T

    # vamos recorriendo S 1 por 1 para ver cuando matchean T
    for i in range(n):
        # Si matchea T movemos apuntador de T 
        if S[i] == T[j]:
            j += 1
    # Al final es len(S) - los que matchea con T
    return n - j




def min_operations_to_reverse(S):
    T = [::-1]
    n = len(S)

    j = 0

    for i in range(n):
        if S[i] == T[j]:
            j += 1
    
    return n - j