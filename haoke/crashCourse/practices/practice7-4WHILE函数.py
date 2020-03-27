# 7-4 比萨配料 ：编写一个循环，提示用户输入一系列的比萨配料，并在用户输入'quit' 时结束循环。每当用户输入一种配料后，都打印一条消息，说我们会在比萨
# 中添加这种配料。
message = '您想在pizza中添加什么配料？'
message += '\n输入quit退出点菜哦~'
ingredient = ''
while ingredient != 'quit':
    ingredient = (input(message))
    print('我们会在pizza中添加'+ingredient+'的！')
# 7-5 电影票 ：有家电影院根据观众的年龄收取不同的票价：不到3岁的观众免费；3~12岁的观众为10美元；超过12岁的观众为15美元。请编写一个循环，在其中询问用
# 户的年龄，并指出其票价。
age = [3,12]
price = ['0','10','15']
message1 = 'Please input your age:'
message1 += '\nInput quit to quit.'
user_age = ''
while user_age != 'quit':
    user_age = input(message1)
    if user_age == 'quit':
        break
    elif int(user_age) < age[0]:
        print('The price of the ticket is:'+price[0])
        continue
    elif int(user_age) < age[1]:
        print('The price of the ticket is:'+price[1])
        continue
    else:
        print('The price of the ticket is:'+price[2])

# 7-6 三个出口 ：以另一种方式完成练习7-4或练习7-5，在程序中采取如下所有做法。
# 在while 循环中使用条件测试来结束循环。
# 使用变量active 来控制循环结束的时机。
# 使用break 语句在用户输入'quit' 时退出循环。

#练习7-4变体
message = '您想在pizza中添加什么配料？'
message += '\n输入quit退出点菜哦~'
active = True
while active:
    ingredient = (input(message))
    if ingredient == 'quit':
        active = False
    else:
        print('我们会在pizza中添加'+ingredient+'的！')

#练习7-5变体
age = [3,12]
price = ['0','10','15']
message1 = 'Please input your age:'
message1 += '\nInput quit to quit.'
active1 = True
while active1:
    user_age = input(message1)
    if user_age == 'quit':
        active1 = False
    elif int(user_age) < age[0]:
        print('The price of the ticket is:'+price[0])
    elif int(user_age) < age[1]:
        print('The price of the ticket is:'+price[1])
    else:
        print('The price of the ticket is:'+price[2])
    

# 7-7 无限循环 ：编写一个没完没了的循环，并运行它（要结束该循环，可按Ctrl +C，也可关闭显示输出的窗口）。

