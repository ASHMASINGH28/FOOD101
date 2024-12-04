def slope_of_a_cubic(t,x):
    if len(t)==4:
        slope=(3*t[0]*x**2) + (2*t[1]*x**1)+ (t[2])
        return slope
        
    else:
        print("Provide the tuple with four characters")
    

