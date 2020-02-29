# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
#  示例： 
# 
#  输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
#  
#  Related Topics 链表


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        vir_head = ListNode(-1)

        vir_h = vir_head
        while l1 and l2:
            if l1.val <= l2.val:
                vir_h.next = l1
                l1 = l1.next
            else:
                vir_h.next = l2
                l2 = l2.next
            vir_h = vir_h.next

        vir_h.next = l1 if l1 else l2

        return vir_head.next
# leetcode submit region end(Prohibit modification and deletion)
