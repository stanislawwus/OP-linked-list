class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def loop_size(node):
    visited = {}
    cur = node
    i = 0
    while cur not in visited:
        visited[cur] =  i
        i+=1
        cur = cur.next
    return len(visited) - visited[cur]