import time
def analayser(nums):
    start= time.time()
    j=0
    total=0
    for i in nums:
           total +=i  
           j=j+1
    end= time.time()
    execution_time=end-start
    return total,j,execution_time

resultat = analayser([1+2+3+4+5+6+7+8])
print(resultat)