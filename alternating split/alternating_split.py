class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError   
    res = Context(head, head.next)    
    first = res.first
    second = res.second
    head_cur = head.next.next
    i = 1
    while True:
        if i%2:
            first.next = head_cur
            first = first.next
        else:
            second.next = head_cur
            second = second.next
        i+=1
        if head_cur is None:
            break
        head_cur = head_cur.next
    return res