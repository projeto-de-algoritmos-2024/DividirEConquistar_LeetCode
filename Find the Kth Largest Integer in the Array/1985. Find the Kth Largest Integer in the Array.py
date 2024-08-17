class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:

        def mom(arr: List[int], k: int) -> int:

            if len(arr) <= 5:
                return sorted (arr)[k] # ordena e acha a kesima posição

        medianas = []

        for i in range(0, len(arr), 5):
            grupo = sorted(arr[i:i + 5])
            medianas.append(grupo[len(grupo) // 2]) # 2 é o índice do terceiro elemento, adiciona a mediada calculada na lista

        pivo = mom(medianas, len (medianas) // 2)
