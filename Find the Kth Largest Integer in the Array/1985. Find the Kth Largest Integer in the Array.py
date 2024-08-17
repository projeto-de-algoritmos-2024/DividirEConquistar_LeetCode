class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:

        def mom(arr: List[int], k: int) -> int:

            if len(arr) <= 5:
                return sorted (arr)[k] # retorna os números ordenados e acha a kesima posição

        medianas = []
        
