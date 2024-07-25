class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        

        #ordenar da maior diferenca de preco para a menor
        copiaOrdenada = sorted(costs, reverse= True, key=lambda person : abs(person[0] - person[1]))
        
        #Incluir na solucao se for compativel, ou seja, a e b devem ter a msm qtd de pessoas e sempre devemos optar pelo mais barato
        n = (len(costs))/2
        a = 0
        b = 0
        totalCost = 0
        
        for person in copiaOrdenada:
           if person[0] < person[1]: #a ta mais barato que b
               if a < n:
                   a = a+1
                   totalCost = totalCost + person[0]
               else:
                   b = b+1
                   totalCost = totalCost + person[1]
           else: # b ta mais barato que a
                if b < n:
                   b = b+1
                   totalCost = totalCost + person[1]
                else:
                   a = a+1
                   totalCost = totalCost + person[0]
                   
        return totalCost
                   