"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    grid[i][j] is '0' or '1'.

Mental Trigger: Grid -> DFS / BFS
DFS -> You need to explore everything (xount, exist, mark, explore)
BFS -> you look for shortest path, level by level trversal (shortest, min, distance)

"""

def numIslands(grid):
    if not grid:
        return 0
    
    rows = len(grid) # Obtenemos len rows
    cols = len(grid[0]) # Obtenemos len de cols

    def dfs(r, c):
        # validamos limites, y que la celda no sea agua
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
            return
        # Si llega hasta aquí, es porque es una isla. así que la destruimoS
        # para evitar contarla again, jiji marcamos como visitada
        grid[r][c] = "0"

        # Como hay isla, necesito checar a los vecinos para
        # hacer lo mismo de marcarlos
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    
    count = 0

    # Iteramos filas
    for r in range(rows):
        # Iteramos cols
        for c in range(cols):
            # Si esta es 1 quiere decir que puede estar rodeada de 1
            if grid[r][c] == "1":
                dfs(r, c)
                count += 1
    
    return count