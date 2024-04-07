def get_nth(node, index):
    while node:
        index -= 1
        if index == -1:
            return node
        node = node.next
    raise IndexError