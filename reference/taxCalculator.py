class TaxCalculator:
    '''税后工资计算器'''
    def __init__(self, salary=0):
        self.salary_levels = [0, 3000, 12000, 25000, 35000, 55000, 80000]
        self.tax_levels = [0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]
        self.cum_taxes = [0]
        self.salary = salary

    def get_cum_taxes(self):
        if len(self.cum_taxes) > 1:
            return self.cum_taxes

        for i in range(1, len(self.salary_levels)):
            amount = self.salary_levels[i] - self.salary_levels[i - 1]
            cum_tax = amount * self.tax_levels[i - 1]
            self.cum_taxes.append(cum_tax)
        return self.cum_taxes

    def get_tax_level(self):
        for i in range(1, len(self.salary_levels)):
            if self.salary > self.salary_levels[i - 1] and self.salary <= self.salary_levels[i]:
                return i

        return len(self.tax_levels)

    def get_tax(self, tax_level):
        remain = self.salary - self.salary_levels[tax_level - 1]
        remain_tax = remain * self.tax_levels[tax_level - 1]
        return remain_tax + sum(self.cum_taxes[:tax_level])

    def show_salary(self):
        tax_level = self.get_tax_level()
        tax = self.get_tax(tax_level)
        after_tax_salary = self.salary - tax
        print('您的税后工资为：\n'+str(after_tax_salary) + '元')
        print('您需缴纳所得税为：\n'+str(tax) + '元')

    def main(self):
        while True:
            self.salary = input("请输入您每月税前工资/输入'quit'退出：")
            try:
                if self.salary == 'quit':
                    break
                else:
                    self.salary = int(self.salary)

            except ValueError:
                print('您输入的数据有误哦\n')
                continue

            else:
                self.get_cum_taxes()
                self.show_salary()
