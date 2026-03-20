"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

 

Constraints:

    1 <= nums.length <= 104
    0 <= nums[i] <= 105

"""
"""
Mental trigger: Reach end, max jump -> Greedy
Track the furthest index you can reach
If at any point you can´t move forward -> fail
"""

def canJump(nums):
    # Empiezas en este numero
    max_reach = 0
    # vamos numero por numero recorriendo el array
    for i in range(len(nums)):
        # si tu index > max_reach quiere decir que tu index esta 
        # en un lugar non reachable y por eso es false
        if i > max_reach:
            return False
    max_reach = max(max_reach, i + nums[i])

    return True

# Practicando doble

def canJump(nums):
    max_reach = 0

    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])

    return True