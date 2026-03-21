"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

 

Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""

"""
product except self / no division -> prfijo + sufijo
result[i] = (producto of left side) * (product of right side)
"""

def productExceptSelf(nums):
    res = [1] * len(nums)

    prefix = 1
    # empieza a hacer iteraciones de la parte izquierda
    for i in range(len(nums)):
        # Como no cuenta el actual entonces prefix empieza en 1
        res[i] = prefix
        # y este es para la siguiente iteracion
        prefix *= nums[i]
    # como no cuenta el actual suffix es 1
    suffix = 1
    # este encambio va de derecha a izquierda
    for i in range(len(nums)-1, -1, -1):
        # Le estamos de una vez multiplicando elsufijo
        res[i] *= suffix
        # y ponemos el sufijo siguiente
        suffix *= nums[i]

    return res


def productExceptSelf(nums):
    suffix = 1
    prefix = 1
    res = [1] * len(nums)
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    for i in range(len(nums), -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
    
    return res
    