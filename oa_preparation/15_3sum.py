"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

 

Constraints:

    3 <= nums.length <= 3000
    -105 <= nums[i] <= 105
"""

"""
Mental Trigger: 3 numbers sum -> Sort + 2 pointers
Idea, sort array, fix one number, use two pointers to find the other two
"""


def threeSum(nums):
    nums.sort()
    res = []

    for i in range(len(nums)):
        # la primera validacion hace que no entre si es
        # and the value of this and the prev one is not the same
        if i > 0 and nums[i] == nums[i-1]:
            continue
        #  l empieza al lado de i
        l = i + 1
        # r empieza a la derecha
        r = len(nums) - 1

        # Estos son los apuntadores
        while l < r:

            total = nums[i] + nums[l] + num[r]

            if total == 0:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                # Te aseguras que l no es el mismo que el anterior
                # Sino el que faltaria seria el mismo de r
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            # como estan ordenados entonces quiere decir que l esta muy a la izquierda
            elif total < 0:
                l += 1
            # Si total es mayor a 0 quiere decir que r esta muy grande
            else:
                r -= 1
        return res

# practica

def threeSum(nums):
    nums.sort()
    res = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i -1]:
            continue
        
        l = i + 1
        r = len(nums) - 1

        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total == 0:
                res.append([i, l, r])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            elif total < 0:
                l += 1
            else:
                r += 1
        
        return res