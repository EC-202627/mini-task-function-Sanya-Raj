def calculate_fine():
    M = str(input())
    N = int(input())
    P = int(input())
    Q = int(input())
    
    fine = float(N * 5)

    if fine > 200:
        fine = 200.0

    print(f"Book: {M}")
    print(f"Days overdue: {N}")
    print(f"Fine: Rs. {fine}")
    
    return fine

calculate_fine()
