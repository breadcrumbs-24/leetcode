"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

 

Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 400

"""

"""
Choose skip or max val -> DP
at each house skip and rob

2 choices
1. Rob it -> take money + skip prev house
2. Skip it -> take whatever you had before

-------
Core formula 
new = max(rob1 * current, rob2)

rob1 = money up to house i -2
rob2 = money up to house i -1 
"""



def rob(nums):
    # Start at 0 because you havent robbed nothing yet
    # Dinero de hace dos casas atras
    rob1 = 0
    # Dinero de una casa atras
    rob2 = 0

    # Empiezas a ir casa por casa
    for n in nums:
        # Roba esta casa e ignora la anterior
        rob_now = rob1 + n
        # Rob now or skip now
        newRob = max(rob_now, rob2)
        # Ahora rob2 se vuelve dos atras entonces se vuelve rob1
        rob1 = rob2
        # y el newRob que es el max se vuelve la evaluacion del prev one
        rob2 = newRob

    return rob2





# OTra practica
def robHouse(nums):
    rob1 = 0
    rob2 = 0

    for n in nums:
        new_rob = max(rob1 + n ,rob2)
        rob1 = rob2
        rob2 = new_rob

    return rob2

