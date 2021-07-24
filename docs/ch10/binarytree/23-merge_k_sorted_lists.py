# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        sub_list = []
        for i in lists:
            while i:
                sub_list.append(int(i.val))
                i = i.next
        
        sub_list = list(sorted(sub_list))
        
        result_list = None
        pre_node = None
        cur_node = None
        
        for i in range(len(sub_list)):
            if i == 0:
                result_list = ListNode(sub_list[i])
                pre_node = result_list
            else:
                pre_node.next = ListNode(sub_list[i])
                pre_node = pre_node.next
        
        return result_list