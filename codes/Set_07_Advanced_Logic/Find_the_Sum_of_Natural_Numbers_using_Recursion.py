def sum_of_natural_numbers(n):
    if n<=1:
        return n
    else:
        return n + sum_of_natural_numbers(n-1)
    
num=int(input("Emter a number: "))
print("Sum of natural numbers: ", sum_of_natural_numbers(num))