from class_Tax import Tax

while True:
    salary = input("请输入您每月税前工资/输入'quit'退出：")
    try:
        if salary == 'quit':
            break
        else:
            salary = int(salary)

    except ValueError:
        print('您输入的数据有误哦\n')
        continue
    
    else:
        salary = Tax(salary)
        salary.calculate_tax()
