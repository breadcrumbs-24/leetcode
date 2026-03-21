"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
            3
           /  \
          9   20
             /   \
            15    7

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

 

Constraints:

    The number of nodes in the tree is in the range [0, 2000].
    -1000 <= Node.val <= 1000

"""

"""
Mental trigger -> BFS (queue)
Use a queue
Add children to queue
"""

# this is a double ended queue
# It can be fifo or lifo
# append(x) append to the right appendleft(x)
# extend(iterable) extendleft(iterable)

#pop() and popleft()
# remove(value) remove the first occurence of the specified value
from collections import deque

# root es un TreeNode
def levelOrder(root):

    # Si el arbol está vacío se regresa un array vacío
    if not root:
        return []
    
    res = []
    # se crea el queue
    queue = deque([root])

    # Mientras haya nodos en el nivel
    while queue:
        level = []
        # Este es el numero de nodos en el nivel actual
        for _ in range(len(queue)):
            # Tomamos el de la izquierda y lo agregamos a la lista de niveles
            node = queue.popleft()
            # Agrega su valor al nivel
            level.append(node.val)

            # Estos son los niveles hijos
            if node.left:
                # Si hay este nodo lo agregamos al queue
                queue.append(node.left)
            if node.right:
                # Si hay este nodo lo agregamos al queue
                queue.append(node.right)
        # Agrega el array de nivel a la respuesta
        res.apppend(level)
    return res

from collections import dequeue
def levelOrder(root):
    res = []

    if not root:
        return []
    
    queue = dequeue([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            
        res.append(level)

    return res