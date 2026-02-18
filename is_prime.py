def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    limit = int(num ** 0.5) + 1
    for i in range(3, limit, 2):
        if num % i == 0:
            return False
    return True

def main():
    try:
        M = int(input().strip())
        N = int(input().strip())
    except Exception:
        print("Please enter two integers.")
        return
    if M > N:
        M, N = N, M
    total = 0
    for i in range(M, N + 1):
        if is_prime(i):
            total += i
    print(total)

if __name__ == "__main__":
    main()