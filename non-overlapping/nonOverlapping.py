class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
         #ordenar do menor fim para o maior
        copiaOrdenada = sorted(intervals, key=lambda inter: (inter[0]))
        
        #Incluir na solucao se for compativel
        intervalosCompativeis = 0
        fim = 0
        
        for inter in copiaOrdenada:
           if inter[0] >= fim: # é compativel pq comeca depois do fim do ultimo
               intervalosCompativeis += 1
               fim = inter[1]
               
            
        return len(intervals) - intervalosCompativeis