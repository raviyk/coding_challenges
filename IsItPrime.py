def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    import math
    a = int(input())
    #a_sqrt = int(math.sqrt(a))
    a_half = a//2
    for i in range(2, a_half):
        if a % i == 0:
            print("NO")
            exit()
    print("YES")

    return 0


if __name__ == '__main__':
    main()
