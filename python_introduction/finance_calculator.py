income = float(input("Enter your monthly income: ")) #prompt the user for monthly income
expenses = float(input("Enter your total monthly expenses: ")) #prompt the user for monthly expenses

monthly_savings = income - expenses #calculate monthly savings
interest_rate = 0.05 #annual interest rate = 5%
annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * interest_rate) #project savings after one year with simple interest

#display results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${annual_savings}.")
