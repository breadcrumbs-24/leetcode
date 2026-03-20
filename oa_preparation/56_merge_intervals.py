"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Example 3:

Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.

 

Constraints:

    1 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 104

Ordering, so sort
Greedy, best decision rightnow, as you swipe left to right 
Greedy only works if A local optimal choice leads to a global optimal solution
Mental Trigger: Intervals + overlap -> sort + greedy
"""

def merge(intervals):
    # Esto va a ordenarlos de forma ascendente basado en
    # x[0] que es el primer numero
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]] # seria el primer key pair

    # Aqui cada start y end van a ser los key pairs
    for start, end in intervals[1:]:
        # Del ultimo mergeado el segundo key
        last_end = merged[-1][1]

        # Esto quiere decir que el key pair que tengo el
        # primero va en medio del merged keypair
        if start <= last_end:
            # Como sabemos que lo anterior se cumplio, ahora, el
            # segundo value del keypair, va a ser el end, que es del intevrval
            # keypair analizado o el last_end, depende de quien sea el maximo
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    
    return merged



# Reescribiendolo por si me quedaron dudas
def merge(intervals):
    intervals.sort(ley:lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]

        if start < merged[-1][1]:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    
    return merged

