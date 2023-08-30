# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # def setValue( node, val):
        #     node1 = ListNode( val, None)
        #     node.next = node1
        #     node = node.next

        dummy = ListNode()
        result = dummy

        while list1 is not None and list2 is not None:
            val = 0
            if list1.val < list2.val:
                val = list1.val
                list1 = list1.next
            else:
                val = list2.val
                list2 = list2.next
            temp = ListNode(val, None)
            dummy.next = temp
            dummy = dummy.next

        # while list1 is not None :
        #     temp = ListNode(list1.val,None)
        #     dummy.next = temp
        #     dummy = dummy.next
        #     list1 = list1.next

        # while list2 is not None :
        #     temp = ListNode(list2.val,None)
        #     dummy.next = temp
        #     dummy = dummy.next
        #     list2 = list2.next

        if list1 is not None:
            dummy.next = list1

        if list2 is not None:
            dummy.next = list2

        return result.next


def getExecutable(*args):
    return Solution().mergeTwoLists(*args)
