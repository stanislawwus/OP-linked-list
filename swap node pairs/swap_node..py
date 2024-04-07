class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
def swap_pairs(head):
    if not head or not head.next:
        return head
    head_n = head.next
    node_cur = head
    while node_cur and node_cur.next:
        _ = node_cur.next
        node_cur.next = node_cur.next.next
        _.next = node_cur
        node_cur = node_cur.next
        if node_cur and node_cur.next:
            _.next.next = node_cur.next
    return head_n