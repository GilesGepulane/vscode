monthly_salary = float(input("Monthly Salary:"))

if monthly_salary >= 30.000:
    print("eligible")
    loan_amount  = float(input("loan amount:"))
    loan_check = loan_amount * 10
    if loan_amount <= loan_check:
        print("eligible")
        months = int(input("Months:"))
        interest = loan_amount * 0.10
        loan_amount = interest + loan_amount
        payable = loan_amount/months
        print("Total:",payable)
    else:
        print("not eligible")
else:
    print("not eligible")