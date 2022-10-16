money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

while money_capital + salary >= spend * (1 + increase) ** month:
    money_capital = money_capital + salary - spend * (1 + increase) ** month
    month += 1

print(month)
