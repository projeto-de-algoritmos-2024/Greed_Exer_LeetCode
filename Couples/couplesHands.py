class Solution:         
     def minSwapsCouples(self, row: List[int], ans = 0) -> int:

        for i in range(0,len(row),2): #andar pelo num. pares

                j = row.index(row[i]^1) #achar o index do par do row[i]
                row[i+1], row[j] = row[j], row[i+1] #trocar de lugar
                ans+= row[j] != row[i+1] #se forem diferentes, tem inversao

        return  ans