#Student: Avakian Andranik

revenue = int(input("Your annual revenue:"))
costs = int(input("Yor annual costs:"))
profit = revenue - costs
if revenue >= costs:
    print("Your company got profit!")
    profitability = profit/revenue
    print(f"Your profitability is {profitability}. Well done!")
    staff = int(input("How many people work in your company?"))
    profit_employee = profit / staff
    print(f"Your profit per employee: {profit_employee}")
else:
    print("Your company got loss")
