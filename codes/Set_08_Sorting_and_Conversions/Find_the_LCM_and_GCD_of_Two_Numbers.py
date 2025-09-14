def compute_lcm(x,y):
    lcm=(x*y)//compute_gcd(x,y)
    return lcm
def compute_gcd(x,y):
    while y:
        x,y=y,x%y
    return x
num1=int(input("Enter first number: "))
num2=int(input("Enter the second number: "))
print("LCM: ", compute_lcm(num1,num2))
print("GCD: ", compute_gcd(num1,num2))