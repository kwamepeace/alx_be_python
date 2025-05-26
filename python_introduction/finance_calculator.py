#Collecting income and expenses data
monthly_income = int(input('Enter your monthly income: '))
monthly_expenses = int(input('Enter your total monthly expenses: '))

# Calculating monthly income
monthly_savings = income - expenses

#Calculating projected annual savings
projected_savings = str(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

#outputting results
print('Your monthly savings are ' + str(monthly_savings) + '.')
print ("Projected savings after one year, with interest, is :", "$" + projected_savings)
