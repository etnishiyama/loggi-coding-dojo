input_n = 3
numbers = [(24, 1), (4358, 754), (305,794)]
expected = [34, 1998, 1]

def test(n, numbers, expected):
    for i in range(n):
        a,b = numbers[i]
        assert solution(a,b) == expected[i]

def solution(v1, v2):
    return -1

def main(n, numbers, expected):
    pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':    
    test(input_n, numbers, expected)
