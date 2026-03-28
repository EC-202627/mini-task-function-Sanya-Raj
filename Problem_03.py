def calculate_fine():
    M = str(input())
    N = int(input())
    
    fine = float(N * 5)

    if fine > 150:
        fine = 150.0

    print(f"Book: {M}")
    print(f"Days overdue: {N}")
    print(f"Fine: Rs. {fine}")

    if fine == 150:
        print(f"You have accumulated the maximum fine of INR: 150.0")
     


    return fine

calculate_fine()