class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_test_node(case_list: list) -> ListNode:
    case_list_len = len(case_list)
    if case_list_len == 0:
        return None
    if case_list_len == 1:
        return ListNode(case_list[0], None)

    node_next = None
    node_curr = None

    for n in case_list[::-1]:
        if node_next is None:
            node_next = ListNode(n, None)
        else:
            node_curr = ListNode(n, node_next)
            node_next = node_curr
    
    return node_curr

def print_list_node(head: ListNode):
    while True:
        if head:
            print(head.val)
            if head.next:
                head = head.next
            else:
                break
        else:
            print([])
            break