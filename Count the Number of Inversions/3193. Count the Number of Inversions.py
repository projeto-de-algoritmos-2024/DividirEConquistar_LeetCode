class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        mod = 10*9 + 7 
        
        dp = [1] + [0] * k
        
        prefix_sum = [0] * (k + 2)
        
        for numero_atual in range(1, n + 1):
            for contagem_inversos in range(1, k + 1):
                
                dp[contagem_inversos] = (prefix_sum[contagem_inversos + 1] - 
                                         prefix_sum[max(0, contagem_inversos - (numero_atual - 1))]) % mod
            
            for indice in range(1, k + 2):
                prefix_sum[indice] = (prefix_sum[indice - 1] + dp[indice - 1]) % mod    

        return dp[k]