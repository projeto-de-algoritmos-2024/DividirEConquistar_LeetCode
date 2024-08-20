class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # se nums1 for maior que nums2, troca
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1 

        x, y = len(nums1), len(nums2)
        low, high = 0, x
  
        # loop até ate chegar a 0
        while low <= high:
            # partição de nums1 e nums2 
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            # os valores máximos e mínimos das partições
            maxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minX = float('inf') if partitionX == x else nums1[partitionX]
            
            maxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minY = float('inf') if partitionY == y else nums2[partitionY]

            # verificar se a partição tá correta
            if maxX <= minY and maxY <= minX:
                # se a soma dos tamanhos dos arrays for par, a mediana é a média dos maiores dos menores valores
                if (x + y) % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
                # senão a mediana é o maior dos menores valores
                else:
                    return max(maxX, maxY)
            elif maxX > minY:
                #  ajusta a partição em `nums1` para a esquerda
                high = partitionX - 1
            else:
                #  ajusta a  partição em `nums1` para a direita
                low = partitionX + 1

        raise ValueError("Inválida")
