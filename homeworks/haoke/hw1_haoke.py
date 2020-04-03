salary_ori = input('请输入您每月税前工资：')
salary = int(salary_ori)
tax1 = 0.03
salary1 = 3000
tax2 = 0.1
salary2 = 12000
tax3 = 0.2
salary3 = 25000
tax4 = 0.25
salary4 = 35000
tax5 = 0.3
salary5 = 55000
tax6 = 0.35
salary6 = 80000
tax7 = 0.45
if salary <= salary1:
    print("您的税后工资为：")
    print(salary-salary*tax1)
if salary > salary1 and salary <= salary2:
    print("您的税后工资为：")
    print(salary-salary1*tax1-(salary-salary1)*tax2)
if salary > salary2 and salary <= salary3:
    print("您的税后工资为：")
    print(salary-salary1*tax1-(salary2-salary1)*tax2-(salary-salary2)*tax3)
if salary > salary3 and salary <= salary4:
    print("您的税后工资为：")
    print(salary-salary1*tax1-(salary2-salary1)*tax2-(salary3-salary2)*tax3-(salary-salary3)*tax4)
if salary > salary4 and salary <= salary5:
    print("您的税后工资为：")
    print(salary-salary1*tax1-(salary2-salary1)*tax2-(salary3-salary2)*tax3-(salary4-salary3)*tax4-(salary-salary4)*tax5)
if salary > salary5 and salary <= salary6:
    print("您的税后工资为：")
    print(salary-salary1*tax1-(salary2-salary1)*tax2-(salary3-salary2)*tax3-(salary4-salary3)*tax4-(salary5-salary4)*tax5-(salary-salary5)*tax6)
if salary > salary6:
    print("您的税后工资为：")
    print(salary-salary1*tax1-(salary2-salary1)*tax2-(salary3-salary2)*tax3-(salary4-salary3)*tax4-(salary5-salary4)*tax5-(salary6-salary5)*tax6-(salary-salary6)*tax7)
