class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def linked_list_from_string(s):
    _ = s.split(" -> ")[::-1][1:]
    main = None
    next = None
    for i in range(len(_)):
        _n = main
        _d = _[i]
        next = main
        main = Node(_d) if _n is None else Node(_d, _n)
    return main