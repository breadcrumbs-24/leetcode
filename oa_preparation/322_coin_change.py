"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0

 

Constraints:

    1 <= coins.length <= 12
    1 <= coins[i] <= 231 - 1
    0 <= amount <= 104

"""

"""
Minimum or best combination -> DP
dp[i] = minimum coins needed to make amount i
dp[0] = 0
dp[i] = min(dp[i], dp[i - coin] + 1)
"""

def coinChange(coins, amount):
    # Esto es con el objetivo de crear un array que apunte al infinito
    # porque buscamos el minimo
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0
    # lo que queremos encontrar es dp[amount]
    # Empezamos en dp[1] porque el dp[0] ya lo tenemos
    for i in range(1, amount + 1):
        # Aquí itera sobre cada una de las monedas
        # Con el fin de intentar con cada una de las monedas
        for coin in coins:
            # Si es menor no cuenta y no la puedes usar, ya que buscas
            # como hacer i 
            if i - coin >= 0:
                # Siendo dp[i] uno más actualizado o uno encontrado antes
                # al inicio dp[i] va a tirar al infinito
                # dp[i-coin] nace porque no necesitas el anterior, necesitas el valor anterior
                # con el que hiciste dp[i-coin] porque sino se va a pasar y luego le agregas el +1
                # porque estas retornando el número de monedas
                # la linea mas importante para i = min(dp[i]m dp[i-coin] + 1)
                dp[i] = min(dp[i], dp[i - coin] + 1)



def coinChange(coins, amount):
    dp = [float("inf")] * amount +1
    dp[0] = 0

    for i in range(1, amount + 1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], dp[i-coin] +1)
    
    return dp[amount] if dp[amount] != float("inf") else -1
