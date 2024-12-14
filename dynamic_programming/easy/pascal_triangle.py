"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above 
        1
      1   1
    1   2   1
  1   3   3   1
1   4   5   4   1

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
"""

# F(1) = [1]
# F(2) = F(1), [F(1)[0], F(1)[-1]]
# F(3) = F(1), F(2), [F(2)[0], F(2)[0] + F(2)[1] ,F(2)[-1]]
# F(4) = F(1), F(2), F(3),  [F(3)[0], F(3)[0] + F(3)[1],  F(3)[1] + F(3)[2]  ,F(3)[-1]]

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows == 1: return res
        # el primer loop es para crear cada row
        for i in range (2, numRows+1):
            # setear los valores iniciales
            tmp = [1]
            #el segundo loop es para cada array del row
            for j in range(0, i-2):
                tmp.append(res[i-2][j] + res[i-2][j+1])
            #seteamos valores finales
            tmp.append(1)
            res.append(tmp)

        return res
