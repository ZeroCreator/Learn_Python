with open('numbers.txt', 'r') as f:
    for line in f:
        n = int(f.readline())
        print(n, type(n))