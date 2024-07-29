class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:

        #ordenar do menor deadline para o maior
        courses.sort(key=lambda co: co[1])
        #trocar sorted por sort pq nao vamos ligar pra boas praticas agr, vamos pela memoria
        
        #Incluir na solucao se for compativel, é possível acabar o curso antes do deadline dele
        #Usar um max heap para manter o curso de maior duracao em cima e ir substituindo
        
        heap = []
        tempoTotal = 0
        
        for duration, deadline in courses:
           if tempoTotal + duration <= deadline: 
               tempoTotal += duration
               heapq.heappush(heap, -duration) #inclui na nossa solucao (heap) e coloca negativo para a maior
               #                                duracao ficar em cima, já que é um max heap
               
           elif heap and -heap[0] > duration:
               tempoTotal += duration + heap[0] #como ja ta negativo, so soma
               heapq.heapreplace(heap, -duration)
                   
        return len(heap)
                   