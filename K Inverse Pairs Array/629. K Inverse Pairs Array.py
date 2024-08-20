class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10**9 + 7  # valor do módulo para manter os números dentro dos limites de inteiros
        
        # A contagem de pares inversos para o número atual de inteiros
        dp = [1] + [0] * k
        
        # Array de soma prefixada para otimizar o loop interno. O tamanho é k+2 para facilitar o acesso e ser 1-indexado
        prefix_sum = [0] * (k + 2)
        
        # Itera através dos inteiros de 1 até n
        for numero_atual in range(1, n + 1):
            # Percorrendo todas as possíveis contagens de pares inversos de 1 até k
            for contagem_inversos in range(1, k + 1):
                # Atualiza a tabela dp pegando a contagem da soma prefixada dentro do intervalo
                # O intervalo corresponde às contagens válidas de pares inversos que podem ser formados com o número atual
                dp[contagem_inversos] = (prefix_sum[contagem_inversos + 1] - 
                                         prefix_sum[max(0, contagem_inversos - (numero_atual - 1))]) % mod
            
            # Atualizando a soma prefixada baseada na tabela dp atualizada
            for indice in range(1, k + 2):
                prefix_sum[indice] = (prefix_sum[indice - 1] + dp[indice - 1]) % mod
                
        # Retorna o número de maneiras de formar k pares inversos com n inteiros
        return dp[k]