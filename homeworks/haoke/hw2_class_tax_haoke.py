class Tax:

    '''参数之间的,之后有个空格：self, salary'''
    def __init__(self):
        self.salary_levels = [0, 3000, 12000, 25000, 35000, 55000, 80000]
        self.tax_levels = [0.03, 0.1, 0.2, 0.25, 0.3, 0.35, 0.45]

    '''命名尽量准确，increase是增加的意思，但是函数逻辑为向salary_levels后面补充一个数值，所以函数名和逻辑之间不匹配
    1 --> 2是增加，向列表中添加元素为append
    sort是不是应该加括号？sort()？'''
    def append_salary_levels(self, salary_level):
        self.salary_levels.append(salary_level)
        self.salary_levels.sort()

    def remove_salary_levels(self, salary_level):
        self.salary_levels.remove(salary_level)

    def increase_tax_levels(self, tax_level):
        self.tax_levels.append(tax_level)
        self.tax_levels.sort

    def remove_tax_levels(self, tax_level):
        self.tax_levels.remove(tax_level)
    
    '''其实主要的目的是分解这个函数，这个函数可以分解成几个互相合作的小函数
    例如：def main():
            salary = input("请输入您的税前工资：")
            #计算出当前工资水平所处的税收等级
            tax_level = get_tax_level(salary)
            #计算出当前工资水平应缴费用
            tax = calculate_tax(salary, tax_level)
            #计算税后工资并打印结果
            display_after_tax_salary(salary, tax)

        main()
    '''
    def progressive_tax(self):
        self.cum_taxes= [0]
        for i in range(1, len(self.salary_levels)):
            self.cum_tax = (self.salary_levels[i] - self.salary_levels[i - 1]) * self.tax_levels[i - 1]
            self.cum_taxes.append(self.cum_tax)
    
    def get_tax_level(self):
        for i in range(1, len(self.salary_levels)):
            if self.pre_salary > self.salary_levels[i - 1] and self.pre_salary <= self.salary_levels[i]:
                self.tax_level = i
                break
            else:
                self.tax_level = len(self.salary_levels)

    def calculate_tax(self):
        self.remain = self.pre_salary - self.salary_levels[self.tax_level - 1]
        self.remain_tax = self.remain * self.tax_levels[self.tax_level - 1]
        self.tax = self.remain_tax + sum(self.cum_taxes[:self.tax_level])

    def calculate_salary(self):
        self.aft_salary = self.pre_salary - self.tax

    def main(self):
        while True:
            self.pre_salary = input("请输入您每月税前工资/输入'quit'退出：")
            try:
                if self.pre_salary == 'quit':
                    break
                else:
                    self.pre_salary = int(self.pre_salary)

            except ValueError:
                print('您输入的数据有误哦\n')
                continue
    
            else:
                self.progressive_tax()
                self.get_tax_level()
                self.calculate_tax()
                self.calculate_salary()
                print('您的税后工资为：\n'+str(self.aft_salary) + '元')
                print('您需缴纳所得税为：\n'+str(self.tax) + '元')
