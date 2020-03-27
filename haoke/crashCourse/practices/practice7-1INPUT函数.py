#7-1 汽车租赁 ：编写一个程序，询问用户要租赁什么样的汽车，并打印一条消息，如“Let me see if I can find you a Subaru”。
message = (input('What brand of car do you want to rent?'))
print('Let me see if I can find you a '+message.title()+'.')
#7-2 餐馆订位 ：编写一个程序，询问用户有多少人用餐。如果超过8人，就打印一条消息，指出没有空桌；否则指出有空桌。
book_message = (input('How many people of you have dinner?'))
number=int(book_message)
if number <= 8:
    print('we have available seats!')
else:
    print('we have no available seats!')
#7-3 10的整数倍 ：让用户输入一个数字，并指出这个数字是否是10的整数倍。
number_10 = int(input('请输入数字：'))
determine = number_10%10
if determine == 0:
    print('这是10的整数倍！')
else:
    print('这不是10的整数倍！')