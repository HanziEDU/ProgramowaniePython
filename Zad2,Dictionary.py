expenses = {"styczen": 2000, "luty": 2400, "marzec": 3400, "kwiecien": 1900, "maj": 2100}

sum_expense = sum(expenses.values())
avg_expense = sum_expense / len(expenses)
last_month = list(expenses.values())[-1]

print(f'minimalna: {min(expenses.values())}')
print(f'maksymalna: {max(expenses.values())}')
print(f'Suma: {sum_expense}')
print(f'Średnia: {avg_expense}')
if last_month > avg_expense:
    print('Jesteś bezpieczny')
else:
    print('Zacznij oszczędzać')