"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

 

Constraints:

    1 <= s.length <= 300
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 20
    s and wordDict[i] consist of only lowercase English letters.
    All the strings of wordDict are unique.

"""

"""
Se puede separar paso a paso? -> DP
define dp
dp[i] = True if s[:i] puede ser construido con palabras
"""

def wordBreak(s, wordDict):
    # Inicializar dp
    dp = [False] * (len(s) + 1)
    # Empieza con dp[0] siempre en true
    dp[0] = True

    for i in range(1, len(s) + 1):
        # va probando palabra por palabra
        # para cada posicion i intentare checar si encaja unaa palabra terminando en i
        for w in wordDict:
            # Luego vamos a checar que si i >= a la longitud de la palabra
            # Recordar que i empieza en 1 y por eso no se le resta 1 a la longitud de la palabra
            # Y hay que tener en cuenta que el dp anterior sea true
            if i >= len(w) and dp[i - len(w)]:
                # aqui la comparamos
                # porque i - len(w) es el inicio de donde estas apuntando
                # el string termina con la palabra
                if s[i - len(w):i] == w:
                    dp[i] = True
    
    return dp[len(s)]



def wordBreak(s, wordDict):
    dp = [False] * len(s)
    dp[0] = True

    for i in range(a, len(s)+ 1):
        for w in wordDict:
            if i >= len(w) and dp[i-len(w)] = True:

                if s[i-len(w):i] == w:
                    dp[i] = True
    
    return dp[len(s)]