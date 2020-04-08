#4-10 切片 ：选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。
friend_list=['chuanqi','chunguang','fengfeng','paopao','bacheng','xuyang']
#打印消息“The first three items in the list are:”，再使用切片来打印列表的前三个元素。
print('The first three friends in the list are:')
print(friend_list[0:3])
#打印消息“Three items from the middle of the list are:”，再使用切片来打印列表中间的三个元素。
print('Three friends in the middle of the list are:')
print(friend_list[2:5])
#打印消息“The last three items in the list are:”，再使用切片来打印列表末尾的三个元素。
print('The last three friends in the list are:')
print(friend_list[-3:])

#4-11 你的比萨和我的比萨 ：在你为完成练习4-1而编写的程序中，创建比萨列表的副本，并将其存储到变量friend_pizzas 中，再完成如下任务。
pizza_list=['Pizzahut',"Papa John's","Domino's Pizza"]
friend_pizza_list=pizza_list[:]
#在原来的比萨列表中添加一种比萨。
pizza_list.append("Chuanky's Pizza")
#在列表friend_pizzas 中添加另一种比萨。
friend_pizza_list.append("Paopao's Pizza")
#核实你有两个不同的列表。为此，打印消息“My favorite pizzas are:”，再使用一个for 循环来打印第一个列表；打印消息“My friend's favorite pizzas are:”，再使用一
#个for 循环来打印第二个列表。核实新增的比萨被添加到了正确的列表中。
print('My favourite pizzas are:')
for pizza in pizza_list:
    print(pizza)
print("My friend's favourite pizzas are:")
for pizza in friend_pizza_list:
    print(pizza)
#4-12 使用多个循环 ：在本节中，为节省篇幅，程序foods.py的每个版本都没有使用for 循环来打印列表。请选择一个版本的foods.py，在其中编写两个for 循环，将各
#个食品列表都打印出来。
my_foods = ['pizza', 'falafel', 'carrot cake']
print('My favourite foods are:')
for food in my_foods:
    print(food)