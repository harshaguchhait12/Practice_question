# Sum of Natural Number  using for loop
def value(n):
    total = 0 
    
    for  i in range(1, n+1):
        total = total + i
        
    return total

print(value(1000))