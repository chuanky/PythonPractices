# 7-8 熟食店 ：创建一个名为sandwich_orders 的列表，在其中包含各种三明治的名字；再创建一个名为finished_sandwiches 的空列表。遍历列
# 表sandwich_orders ，对于其中的每种三明治，都打印一条消息，如I made your tuna sandwich ，并将其移到列表finished_sandwiches 。所有三明
# 治都制作好后，打印一条消息，将这些三明治列出来。
sandwich_orders = ['tuna sandwich','hum sandwich','egg sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print('I made your '+current_sandwich+'.')

print('\nThose sandwiches are ready:')
for sandwich in finished_sandwiches:
    print('\t'+sandwich)

# 7-9 五香烟熏牛肉（pastrami）卖完了 ：使用为完成练习7-8而创建的列表sandwich_orders ，并确保'pastrami' 在其中至少出现了三次。在程序开头附近添加
# 这样的代码：打印一条消息，指出熟食店的五香烟熏牛肉卖完了；再使用一个while 循环将列表sandwich_orders 中的'pastrami' 都删除。确认最终的列
# 表finished_sandwiches 中不包含'pastrami' 。

sandwich_orders = ['tuna sandwich','pastrami sandwich','hum sandwich','pastrami sandwich','egg sandwich','pastrami sandwich',]
print('pastrami sandwich has been sold out.')
while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')
print(sandwich_orders)

# 7-10 梦想的度假胜地 ：编写一个程序，调查用户梦想的度假胜地。使用类似于“If you could visit one place in the world, where would you go?”的提示，并编写一个打印调查
# 结果的代码块。
infor = {}
active=True
while active:
    name = input("What's your name?")
    place = input('If you could visit one place in the world, where would you go?')
    infor[name] = place
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        active = False
for name,place in infor.items():
    print(name.title()+"'s favourite place is "+place.title()+'.')
