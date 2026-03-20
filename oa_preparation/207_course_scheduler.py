"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

 

Constraints:

    1 <= numCourses <= 2000
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All the pairs prerequisites[i] are unique.
"""

"""
Mental Trigger: Dependencies/prerequisites/cycles -> Graph + Cycle Detection (DFS)
Idea: Represent courses as graph, if there is a cycle you can´t finish
Use DFS with 3 states: 0 unvisited, 1 visiting, 2 done.
If you revisit a visiting node -> cycle
"""

def canFinish(numCourses, prerequisites):
    # Creamos un diccionario con los keys de 0 a numCourses -1
    graph = {i: [] for i in range(numCourses)}

    # usando el graph creado anteriormente vamos a appendear los prerequisitos
    # en este ejemplo para el curso {a: [b, c], b: [d]}
    # Quiere decir que para el curso a necesitamos a y b y para el b d
    for a, b in prerequisites:
        graph[a].append(b)
    
    # 0 no visitado, 1 visitando, 2 completo
    # empezamos con todos los cursos en no visitado
    state = [0] * numCourses 

    # Este es el dfs y le pasamos el indice del curso
    def dfs(course):
        # Si llega aquí es falso porque quiere decir que mientras 
        # Visitaba el curso llegue al curso jiji
        if state[course] == 1:
            return False # Esto quiere decir que hay ciclo
        # Esto quiere decir que ya lo visite y esta completo
        if state[course] == 2:
            return True 
        
        # Si llegas hasta aquí quiere decir que el curso no ha sido visitado
        # Lo ponemos como visitando
        state[course] = 1
        # Aqui va uno a uno por los requisitos del curso
        for nei in graph[course]:
            # Basicamente si uno de estos que estoy iterando es falso
            # Devuelve false
            if not dfs(nei):
                return False
        # Ya que itero sobre los requisitos y termine y ninguno fue falso
        # Entonces ese curso puede hacerse le pongo 2 y regreso true
        state[course] = 2
        return True
    
    for i in range(numCourses):
        if not dfs(i):
            return False
    
    return True



# Repasando again
def canfinish(numCourses, prerequisites):
    graph = [i:[] for i in range(numCourses)]

    for cour, prereq in prerequisites:
        graph[cour].append(prereq)

    state = [0] * numCourses

    def dfs(course):

        if state[course] == 1:
            return False
        elif state[course] == 2:
            return True

        state[course] = 1

        for nei in graph[course]:
            if not dfs(nei):
                return False

        state[course] = 2
    
    for i in range(numCourses):
        if not dfs(i):
            return False
    
    return True