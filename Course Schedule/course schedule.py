class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:

        #ordenar do menor deadline para o maior
        copiaOrdenada = sorted(courses, key=lambda course: (course[1], course[0]))
        
        #Incluir na solucao se for compativel, é possível acabar o curso antes do deadline dele
        tempoTotal = 0
        qtdCourses = 0
        
        for course in copiaOrdenada:
           if tempoTotal + course[0] <= course[1]:
               qtdCourses = qtdCourses + 1
               tempoTotal = tempoTotal + course[0]
                   
        return qtdCourses
                   