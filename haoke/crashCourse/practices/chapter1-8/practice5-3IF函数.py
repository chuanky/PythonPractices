#5-3 外星人颜色#1 ：假设在游戏中刚射杀了一个外星人，请创建一个名为alien_color 的变量，并将其设置为'green' 、'yellow' 或'red' 。
alien_color = 'red'
#编写一条if 语句，检查外星人是否是绿色的；如果是，就打印一条消息，指出玩家获得了5个点。
if alien_color == 'green':
    print('You get 5 points!')
    points=5
else:
    points=0
#编写这个程序的两个版本，在一个版本中上述测试通过了，而在另一个版本中未通过（未通过测试时没有输出）。
if points == 5:
    print('You Win!')
#5-4 外星人颜色#2 ：像练习5-3那样设置外星人的颜色，并编写一个if-else 结构。
alien_color1 = 'green'
#如果外星人是绿色的，就打印一条消息，指出玩家因射杀该外星人获得了5个点。
if alien_color1 == 'green':
    print('You get 5 points!')
    points=5
#如果外星人不是绿色的，就打印一条消息，指出玩家获得了10个点。
else:
    print('You get 10 points!')
    points=10
#编写这个程序的两个版本，在一个版本中执行if 代码块，而在另一个版本中执行else 代码块。
if points == 5:
    print('You Lose!')
if points == 10:
    print('You Win!')
#5-5 外星人颜色#3 ：将练习5-4中的if-else 结构改为if-elif-else 结构。
alien_color2 = 'yellow'
#如果外星人是绿色的，就打印一条消息，指出玩家获得了5个点。
if alien_color2 == 'green':
    print('You get 5 points!')
    points=5
#如果外星人是黄色的，就打印一条消息，指出玩家获得了10个点。
if alien_color2 == 'yellow':
    print('You get 10 points!')
    points=10
#如果外星人是红色的，就打印一条消息，指出玩家获得了15个点。
if alien_color2 == 'red':
    print('You get 15 points!')
    points=15
#编写这个程序的三个版本，它们分别在外星人为绿色、黄色和红色时打印一条消息。
if points == 5:
    print('菜狗子')
if points == 10:
    print('菜猫')
if points == 15:
    print('菜菜子')
#5-6 人生的不同阶段 ：设置变量age 的值，再编写一个if-elif-else 结构，根据age 的值判断处于人生的哪个阶段。
age_list=[2,4,13,20,65]
age=int(input('请输入你的年龄：'))
#如果一个人的年龄小于2岁，就打印一条消息，指出他是婴儿。
if age < age_list[0]:
    print('你还是个婴儿~')
#如果一个人的年龄为2（含）～4岁，就打印一条消息，指出他正蹒跚学步。
elif age < age_list[1]:
    print('你还在蹒跚学步呢~')
#如果一个人的年龄为4（含）～13岁，就打印一条消息，指出他是儿童。
elif age < age_list[2]:
    print('你还是个儿童~')
#如果一个人的年龄为13（含）～20岁，就打印一条消息，指出他是青少年。
elif age < age_list[3]:
    print('你还是个青少年~')
#如果一个人的年龄为20（含）～65岁，就打印一条消息，指出他是成年人。
elif age < age_list[4]:
    print('你是个成年人了~')
#如果一个人的年龄超过65（含）岁，就打印一条消息，指出他是老年人。
elif age >= age_list[5]:
    print('你是个成年人了~')
#5-7 喜欢的水果 ：创建一个列表，其中包含你喜欢的水果，再编写一系列独立的if 语句，检查列表中是否包含特定的水果。
#将该列表命名为favorite_fruits ，并在其中包含三种水果。
fruits=['apple','banana','peach','pear','orange']
favorite_fruits=['apple','banana','peach']
#编写5条if 语句，每条都检查某种水果是否包含在列表中，如果包含在列表中，就打印一条消息，如“You really like bananas!”。
if 'apple' in favorite_fruits:
    print("You really like apples!")
if 'banana' in favorite_fruits:
    print("You really like bananas!")
if 'peach' in favorite_fruits:
    print('You really like peaches!')
if 'pear' in favorite_fruits:
    print()
if 'orange' in favorite_fruits:
    print('You really like oranges!')
for fruit in fruits:
    if fruit in favorite_fruits:
        print('You really like '+fruit+'!')