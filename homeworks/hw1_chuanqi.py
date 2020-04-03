salary = ""
salary_levels = [0, 3000, 12000, 25000, 35000, 55000, 80000]
tax_levels = [0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]
cum_taxes = [0]

while salary != "quit":
    salary = input("请输入您每月税前工资：")
    print("running")
    if salary == "quit":
        continue

    salary = int(salary)
    if salary > 80000:
        salary -= salary_levels[-1] * tax_levels[-1]
        print("您的每月税后工资是：" + str(salary))
        continue

    for i in range(1, len(salary_levels)):
        cum_tax = (salary_levels[i] - salary_levels[i - 1]) * tax_levels[i - 1]
        cum_taxes.append(cum_tax + cum_taxes[-1])
        if salary > salary_levels[i - 1] and salary <= salary_levels[i]:
            remain = salary - salary_levels[i - 1]
            salary -= cum_taxes[i - 1]
            salary -= remain * tax_levels[i - 1]

    print("您的每月税后工资是：" + str(salary))

print("calculator closed")