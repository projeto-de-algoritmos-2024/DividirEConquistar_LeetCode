class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(nums1) + len(nums2)
        metade = total // 2

        if len(b)< len(a):
            a, b = b, a

        l, r = 0, len(a) - 1

        while True: 
            i = (1 + r) // 2
            j = metade - i - 2

            a_esquerda = a [i] if i >= 0 else float("inf")
            a_direita = a [i + l] if (i + l) < len(a) else float("inf")
            b_esquerda = n[j] if j >= 0 else float ("-inf")
            b_direita = b[j + l] if (j +l) < len(b) else float('inf')

            if a_esquerda < b_direita and b_esquerda <= a_direita:
                if total % 2:
                    return min(a_direita, b_direita)
                
                return (max(a_esquerda, b_esquerda) + min(a_direita, b_direita)) /2

            elif a_esquerda > b_direita:
                r = i -1

            else:
                l = i+1
