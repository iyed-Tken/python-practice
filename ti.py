import math
def analyze_triangle(a, b , c):
    
    if ( a + b >c) and (a + c> b ) and (c +b> a ):
        print("this triangle is valid ")
        perimetre= a + b + c
        print(f"perimetre = {perimetre }")
        s= perimetre /2  
        aire= math.sqrt(s * (s-a) * (s-b) * (s-c))
        print(f"area= {aire:.4f}")
    else:
     print("these segements cannot create a valid triangle")
analyze_triangle(3,6,7)
#########
def convert_temperature(value, unite):
   Unite= unite.strip().lower()
   if Unite in ['c', 'celsius']:
      c = value
      f = c* 9/5 +32
      k= c + 237.15
      print(f"intiale temperature : {c} c ")
      print(f"temperature in fahreheit is : {f} f ")
      print(f"temperature in kelvin is: {k} k"),
   elif Unite in ["f", "fahrenheit"]:
      f= value
      c= f-32 *5/9
      k= c +273.15 
      print(f"initial temperature is: {f} F")
      print(f" equivalent in celeuis: {c} c ")
      print(f"equivalent in kelvin: {k} K")
   elif Unite in ["k", "kelvin "]:
      k= value 
      if k<0:
         print("Erreur : temperature en kelvin should" \
         " not be smaller than 0")

      c= k - 273.15
      f= c *9/5 +32
      print(f"temperature initiale: {k} k")
      print(f"temperature : {f} f")
      print(f"temperature : {c} c")
   else:
      print("Unite no reconnue")
convert_temperature(50, "c")
##########
def check_leap_year(y):
   if (y % 4== 0 and y %100 !=0) or(y % 400 == 0):
      print(f" the year {y} is a leap year ")
   else:
      print(f"the year {y} is not a leap year")
check_leap_year(2005)
####################
def linear_equation(a, b):
   print(f" solving equation : {a}x + {b}=0")
   if (a!= 0) :

      print(f"x= {-b/a} ")
   elif b==0:
      print("Infinite solutions to this equation ")
   
   else:
      print(f" NO solution to this equation")
linear_equation(0,0)
##################
def minimum(N):
   m= N[0]
   i = 1
   while i< len(N):
      if N[i]<m:
         m= N[i]
      i+=1 
   return m
numbers = [1,3,2,0,8]
print(minimum (numbers))
##########
def minimum(B):
   m= B[0]
   for i in range(1,len(B)):
      if B[i]<m:
         m= B[i]
   return m
numbers= [1,3,5,0]
print(minimum(numbers))
###################
def find_minimum(C):
   if C[0]> C[1]:
      l= C[0]
      s= C[1]
   else:
      l= C[1]
      s= C[0]
   for i in range(2,len(C)):
      if C[i]>l:
         s=l
         l= C[i]
         
      elif C[i]>s:
           
           s= C[i]
   return l,s
arr = [12,45,7,89,34,69,-20]
big1, big2 = find_minimum(arr)
print("Largest: ", big1)
print("Second Largest: ", big2)
##################################
def find_two_bigger(F):
   if F[0]> F[1]:
      M= F[0]
      m= F[0]
   else:
      M= F[1]
      m= F[0]
      for i in range(2, len(F)):
         if F[i]>M:
            M= F[i]
         else:
            m= M
         

      return M,m
numbers= [1,3,5,0,9]
print(find_two_bigger(numbers))
##############################
def find_max_and_min(G):
   if G[0]> G[1]:
      ma= G[0]
      mi= G[1]
   else:
      ma= G[1]
      mi= G[0]
   for i in range (2, len(G)):
      if G[i]> ma:
         ma= G[i]
      else:
        if G[i]<mi:
           mi= G[i]
   return ma,mi
numbers= [1,3,5,0,9]
print(find_max_and_min(numbers))





           
        

   


        
      
   




   
   




    

   

  

    
   


