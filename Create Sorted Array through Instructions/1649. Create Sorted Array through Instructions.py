
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
        mod = 1000000007
        # Inicializa a árvore com tamanho 100000 + 1
        bit = BIT(100000 + 1)
        resultado = 0
        
        for i, num in enumerate(instructions):
            # custo de inserção
            custo_e = bit.soma(num - 1)
            custo_d = i - bit.soma(num)
            resultado += min(custo_e, custo_d)
            resultado %= mod
            

            bit.add(num, 1)
        
        return resultado
