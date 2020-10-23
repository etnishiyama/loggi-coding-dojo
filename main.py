

input_n = 3
numbers = [(24, 1), (4358, 754), (305,794)]
expected = [34, 1998, 1]

def test(n, numbers, expected):
    for i in range(n):
        a,b = numbers[i]
        current_sol = solution(a,b)
        print(current_sol)
        print(expected[i])
        assert  current_sol == expected[i]

def solution(v1, v2):
    v1_int = str(v1)[::-1]
    v2_int = str(v2)[::-1]
    sum_int = int(v1_int) + int(v2_int)
    return int(str(sum_int)[::-1])

def main():
    n = int(input())
    for i 
    pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test(input_n, numbers, expected)
    main()
