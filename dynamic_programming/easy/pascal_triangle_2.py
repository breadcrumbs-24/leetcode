"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
        1
      1   1
    1   2   1
  1   3   3   1
1   4   5   4   1

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33
Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

"""
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        if rowIndex == 0: return res.pop()
        for i in range (1, rowIndex+1):
            # setear los valores iniciales
            tmp = [1]
            #el segundo loop es para cada array del row
            for j in range(0, i-1):
                tmp.append(res[0][j] + res[0][j+1])
            #seteamos valores finales
            tmp.append(1)
            res.pop(0)
            res.append(tmp)
        return res[-1]