"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]

 

Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.

 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

Mental Trigger: 
Top K frequent → Heap OR Bucket Sort

1. Count frequencies
2a. Bucket Sort
Instead of sorting numbers, group numbers by how often they appear
Best for interviews O(n)
2b. Heap. Priority Queue
Always keep track of top k elements.
When k is small, or streaming data
"""
from collections import Counter
def topKFrequent(nums, k):
    # Esto lo que hace es devolver un dictionario tipo
    # Counter({1: 3, 3: 2, 2: 1, 4: 1})
    # 1 appears 3 times ...
    count = Counter(nums)
    # Creamos un bucket por número
    buckets = [[] for _ in range(len(nums) + 1)]
    # Este tambien es super importante porque es como sacas los datos
    for num, freq in count.items():
        # en este caso la frequencia, que de max seria len(nums)
        # y el bucket quedaría todo a la derecha
        # le appendeas el numero porque queremos la lista de nums
        buckets[freq].append(num)
    
    res = []
    # Empezamos de atras para adelante, porque queremos el más grande
    for i in range(len(buckets) - 1, -1, -1):
        # esto para sacar cada uno de los numeros 1 por 1 e ir comprobando 
        # que sea menor a k
        for num in buckets[i]:
            res.append(num)
            if len(res) == k:
                return res




# Repasando


from Collections import Counter
def topKFrequent(nums, k):
    count = Counter(nums)

    buckets = [[] for _ in range(len(nums)+1)]
    res = []
    for num, frequency in count.items():
        buckets[frequency].append(num)
    
    for i in range(len(buckets) - 1, -1, -1):
        for num in bucket[i]:
            res.append(num)
            if len(res) == k:
                return res
