#taking input 
 a=int(input("Enter the value of a:")) 
 b=int(input("Enter the value of b:")) 
 c=int(input("Enter the value of c:")) 
#calculate discriminant 
 d=((b**2)-(4*a*c)) 
#checking if the roots are real or imaginary 
 if (d<0): 
     print("No Real Roots") 
 elif d==0: 
     print("Roots are equal") 
 elif d>0: 
     print("Roots are real and distinct") 
     x1=((-b+(d**0.5)/(2*a)) 
     x2=((-b-(d**0.5)/(2*a)) 
     print(x1,x2)
