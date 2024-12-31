"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105
 

Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
"""

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0, 1]
        power_of_two = 4
        if n < 2:
            return res[:n+1]
        
        for i in range(2, n+1):
            if power_of_two == i:
                # actualizar las potencias de dos
                power_of_two += power_of_two
                # Appendeo 1 porque cada potencia de dos siempre empieza tipo
                #10 100 1000 o sea, con 1
                res.append(1)
            else:
                # esto es para obtener la simetria del pow anterior
                j = i - (power_of_two/2)
                # le sumas 1 porque como estamos en el siguiente pow
                #significa que hemos aumentado un 1
                res.append(res[j] + 1)
        
        return res
  