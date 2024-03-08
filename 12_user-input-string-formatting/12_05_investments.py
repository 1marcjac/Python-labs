# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

principal = int(input ('whats your initial investment: '))
interest_rate = float(input ( 'Whats your interest rate?'))
years_to_invest = int (input('how many years do you want to invest: '))

future_value = principal * ((1 + (interest_rate / 100)) ** years_to_invest)
print(future_value)