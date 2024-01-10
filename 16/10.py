def golden_ratio(i):
    fibonacci_list = [1, 1]
    for ix in range(2, i+1):
        fibonacci_list.append(fibonacci_list[ix-1] + fibonacci_list[ix-2])
    print(fibonacci_list[i] / fibonacci_list[i-1])
