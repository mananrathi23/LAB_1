#taking input 
 a=int(input("Enter the 1st side:")) 
 b=int(input("Enter the 2nd side:")) 
 c=int(input("Enter the 3rd side:")) 
#semi perimeter 
 s=((a+b+c)/3) 
#area using herons formula 
 area=((s*(s-a)*(s-b)*(s-c))**0.5) 
#output 
 print("area is:",area)
