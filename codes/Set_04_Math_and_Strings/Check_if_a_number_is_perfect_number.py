def is_perfect_number(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    if sum==n:
        print("Perfect")
    else:
        print("not perfect")
number=int(input("Enter a number: "))
is_perfect_number(number)


