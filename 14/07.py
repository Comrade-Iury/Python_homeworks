def print_statistics(arr):
    if arr:
        print(f"{len(arr)}\n{average(arr)}\n{min(arr)}\n{max(arr)}\n{median(arr)}")
    else:
        print("0 \n" * 5)


def average(arr):
    return sum(arr) / len(arr)


def median(arr):
    arr.sort()
    if len(arr) % 2 == 0:
        return (arr[int(len(arr) / 2 - 1)] + arr[int(len(arr) / 2)]) / 2
    else:
        return arr[int(len(arr) / 2)]
