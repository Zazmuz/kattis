while True:
    a, b = map(int, input().split())
    if a == b == 0: exit()
    print(f"{a//b} {a%b} / {b}")