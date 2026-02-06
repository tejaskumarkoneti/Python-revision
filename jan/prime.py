def prime(n):
    
    i = 2
    while i < n:
        
        if n % i == 0:
            
            return False
        
        i +=1
    
    return True

num = int(input("Enter a number :"))

if prime(num):
    print("{} is a Prime Number".format(num))
else:
    print("{} is not a Prime Number".format(num))