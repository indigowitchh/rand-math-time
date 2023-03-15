def add(n): #function definition
    if n/10 <= 1: #base case
        return n
    else:
        return n%10+add(int(n/10)) #calls itself
    
print(add(492))
