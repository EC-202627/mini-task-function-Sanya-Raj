def calculate_fine():
    B = str(input())     #Name
    C = int(input())     # No. of days
    D = int(input())     # fine per day 

    fine = float(C *D)   # total fine
    if fine >150:
        fine = 150.0 
    
    print(f"Book: {B}")
    print(f"Days overdue: {C}")
    print(f"Fine: Rs. {fine}")
    return fine

calculate_fine()



