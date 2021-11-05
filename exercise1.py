def odd_sum_calculator(x):
    if x % 2 == 0:
        x=x/2
    else:
        x=(x-1)/2
    calculation = x*(x+1)
    return int(calculation)
        
def avarage_even_calculator(x):
    
    if x % 2 == 0:
        y=x/2
        x = (x + 2)/2
    else:
        y=(x+1)/2
        x = (x + 1)/2
    calculation = x**2/y
    return calculation
    
N=int(input("Enter a number: "))
print("\nSum of odd numbers:",odd_sum_calculator(N),"\nAvarage of even numbers:",avarage_even_calculator(N))
