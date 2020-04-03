class Tax:
    def __init__(self,salary):
        self.pre_salary = salary
        self.salary_levels = [0, 3000, 12000, 25000, 35000, 55000, 80000]
        self.tax_levels = [0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]
        self.cum_taxes = [0]

    def display_salary_levels(self):
        print(self.salary_levels)

    def increase_salary_levels(self,salary_level):
        self.salary_levels.append(salary_level)
        self.salary_levels.sort

    def remove_salary_levels(self,salary_level):
        self.salary_levels.remove(salary_level)

    def display_tax_levels(self):
        print(self.tax_levels)

    def increase_tax_levels(self,tax_level):
        self.tax_levels.append(tax_level)
        self.tax_levels.sort

    def remove_tax_levels(self,tax_level):
        self.tax_levels.remove(tax_level)

    def calculate_tax(self):
        self.cum_taxes= [0]
        for i in range(1, len(self.salary_levels)):
            self.cum_tax = (self.salary_levels[i] - self.salary_levels[i - 1]) * self.tax_levels[i - 1]
            self.cum_taxes.append(self.cum_tax)

        if self.pre_salary > self.salary_levels[-1]:
            self.aft_salary = self.pre_salary - (self.pre_salary - self.salary_levels[-1]) * self.tax_levels[-1] - sum(self.cum_taxes)
            self.tax = self.pre_salary - self.aft_salary
        
        else:
            for i in range(1, len(self.salary_levels)):
                if self.pre_salary > self.salary_levels[i - 1] and self.pre_salary <= self.salary_levels[i]:
                    self.remain = self.pre_salary - self.salary_levels[i - 1]
                    self.aft_salary = self.pre_salary - self.remain * self.tax_levels[i -1] - sum(self.cum_taxes[0:i])
                    self.tax = self.pre_salary - self.aft_salary
        print('您的税后工资为：\n'+str(self.aft_salary) + '元')
        print('您需缴纳所得税为：\n'+str(self.tax) + '元')
