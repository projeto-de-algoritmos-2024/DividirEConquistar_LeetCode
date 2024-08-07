class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        # Inserir o primeiro nó de cada lista na heap
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val, i, lists[i]))
        
        head = ListNode(0)  # nó cabeça
        current = head  # ponteiro atual
        
