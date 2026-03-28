def calculate_fine():
    M = str(input())
    N = int(input())

    fine = float(N * 5)

    print(f"Book: {M}")
    print(f"Days overdue: {N}")
    print(f"Fine: Rs. {fine}")
    return fine

calculate_fine()

