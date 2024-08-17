from typing import List

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        numeros = [int(num) for num in nums]

        def mom(arr: List[int], k: int) -> int:
            # ordena e retorna o kesimo elemento
            if len(arr) <= 5:
                return sorted(arr)[k]
            
            medianas = []
            
            # Dividir a lista em grupos de 5 elementos
            for i in range(0, len(arr), 5):
                grupo = sorted(arr[i:i + 5])
                # 2 é o índice do terceiro elemento, adiciona a mediada calculada na lista
                medianas.append(grupo[len(grupo) // 2])
            
            # Encontrar a mom
            pivo = mom(medianas, len(medianas) // 2)
            
            # lista para armazenar os números menores e maiores que o pivo
            menor = [x for x in arr if x < pivo]
            maior = [x for x in arr if x > pivo]
            
            # x vezes que o pivo aparece no arr inicial
            x_pivo = len(arr) - len(menor) - len(maior)
            
            # buscar o kesimo menor numero
            if k < len(menor):
                # Se k está no grupo de elementos menores que o pivô
                return mom(menor, k)
            elif k >= len(menor) + x_pivo:
                # Se k está no grupo de elementos maiores que o pivô
                return mom(maior, k - len(menor) - x_pivo)
            else:
                # Se k é exatamente o número de vezes que o pivô aparece
                return pivo

        # Encontrar o kesimo maior 
        kth_maior = mom(numeros, len(numeros) - k)
        
        return str(kth_maior)
