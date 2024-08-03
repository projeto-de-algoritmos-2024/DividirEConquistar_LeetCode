class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        for l in lists:
            while l:
                nodes.append(l.val)
                l = l.next
        
        nodes.sort()

        head = ListNode(0) # cria um nó cabeça
        current = head # atual aponta para caebça

        for val in nodes:
            current.next = ListNode(val) # cria um novo nó e liga ao atual
            current = current.next
        
        return head.next
