# Largest of 3 numbers
def find_largest(q,w,e):
    if q > w and q > e:
        return q
    elif w > e:
        return w
    else:
        return e
    
print(find_largest(10,25,100))