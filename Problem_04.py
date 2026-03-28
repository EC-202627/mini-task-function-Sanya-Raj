def calculate_fine():
    M = str(input())
    N = int(input())
    K = float(input())

    fine = float(N * K)
    if fine > 150:
        fine = 150.0

    print(f"Book: {M}")
    print(f"Days overdue: {N}")
    print(f"Fine: Rs. {fine}")
    return fine

calculate_fine()