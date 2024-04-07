class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    node_cur = head
    while node_cur is not None:
        while node_cur.next is not None and node_cur.data == node_cur.next.data:
            node_cur.next = node_cur.next.next
        node_cur = node_cur.next
    return head