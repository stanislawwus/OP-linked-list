class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
        
def stringify(node):
    if node is None:
        return "None"
    res = []
    _d = node.data
    _n = node.next
    while _n is not None:
        res.append(_d)
        _d = _n.data
        _n = _n.next
    res.append(_d)
    res.append('None')
    return " -> ".join([str(x) for x in res])