class BIT:
    # inicializar uma arvore
    def __init__(self, tam: int):
        self.arr = [0] * (tam + 1)
    
    def soma(self, i: int) -> int:
        total = 0
        while i > 0:
            total += self.arr[i]
            i -= i & -i # subtrai o bit menos significativo
        return total
    
    def add(self, i, k):
        # adiciona k ao arr
        while i < len(self.arr):
            self.arr[i] += k
            i += i & -i  # move para o próximo índice usando o bit menos significativo
            
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        
