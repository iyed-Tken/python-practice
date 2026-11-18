import time
def first_program(nums):
    start= time.time()
    j=0
    total=0
    for i in nums:
           total +=i  
           j=j+1
    end= time.time()
    execution_time=end-start
    return total,j,execution_time

resultat = first_program([1+2+3+4+5+6+7+8])
print(resultat)
#===================================================
def second_program(nums):
    
    j=0
    m=1
    for i in range(1,len(nums)):
           if nums[i] >m:
                 m= nums[i]
           j=j+1
    return m,j

resultat = second_program([1,2,3,4,5,6,7,8])
print(resultat)
