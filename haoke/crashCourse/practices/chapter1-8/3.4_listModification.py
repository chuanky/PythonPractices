#3-4 嘉宾名单 ：如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），你会邀请哪些人？请创建一个列表，其中包含至少3个你想邀请的人；然后，使用
#这个列表打印消息，邀请这些人来与你共进晚餐。
friends=['传奇','春哥','泡泡']
message='！我妈喊你来家里吃饭！'
print(friends[0]+message)
print(friends[1]+message)
print(friends[2]+message)
#3-5 修改嘉宾名单 ：你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。
#以完成练习3-4时编写的程序为基础，在程序末尾添加一条print 语句，指出哪位嘉宾无法赴约。
absent1='泡泡'
print(absent1)
#修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
friends[2]='风风'
#再次打印一系列消息，向名单中的每位嘉宾发出邀请。
print(friends[0]+message)
print(friends[1]+message)
print(friends[2]+message)
#3-6 添加嘉宾 ：你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。
#以完成练习3-4或练习3-5时编写的程序为基础，在程序末尾添加一条print 语句，指出你找到了一个更大的餐桌。
#使用insert() 将一位新嘉宾添加到名单开头。
friends.insert(0,'阳哥')
#使用insert() 将另一位新嘉宾添加到名单中间。
friends.insert(2,'李姐')
#使用append() 将最后一位新嘉宾添加到名单末尾。
friends.append('主席')
#打印一系列消息，向名单中的每位嘉宾发出邀请。
print(friends[0]+message)
print(friends[1]+message)
print(friends[2]+message)
print(friends[3]+message)
print(friends[4]+message)
print(friends[5]+message)
#3-7 缩减名单 ：你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。
#以完成练习3-6时编写的程序为基础，在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。
#使用pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进晚餐。
delete1=friends.pop()
message1='！我妈说你不用来了！'
print(delete1+message1)
delete2=friends.pop()
print(delete2+message1)
delete3=friends.pop(0)
print(delete3+message1)
delete4=friends.pop(1)
print(delete4+message1)
#对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
message2='！你还是有饭吃，别忘了来！'
print(friends[0]+message2)
print(friends[1]+message2)
#使用del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程序结束时名单确实是空的。
del friends[0]
del friends[0]
print(friends)