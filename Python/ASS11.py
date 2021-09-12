# FizzBuzz Interview

def num(n):
    if n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    elif n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    else:
        return str(n)
for i in range(1, 31):
    print(num(i))
    
    
