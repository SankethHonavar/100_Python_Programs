def generate_fibonaaci(n):
    fibonaaci_sequence=[0,1]
    for i in range(2,n):
        next_num=fibonaaci_sequence[-1]+fibonaaci_sequence[-2]
        fibonaaci_sequence.append(next_num)
    return fibonaaci_sequence
terms=10
print("Fibonacci Sequence: ", generate_fibonaaci(terms))