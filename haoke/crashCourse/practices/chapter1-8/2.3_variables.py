#个性化消息： 将用户的姓名存到一个变量中，并向该用户显示一条消息。显示的消息应非常简单，如“Hello Eric, would you like to learn some Python today?”。
name='春哥'
message='纯爷们，铁血真汉子！'
print(name+message)
#调整名字的大小写： 将一个人名存储到一个变量中，再以小写、大写和首字母大写的方式显示这个人名。
name1='brother chun'
print(name1.lower())
print(name1.upper())
print(name1.title())
#名言： 找一句你钦佩的名人说的名言，将这个名人的姓名和他的名言打印出来。输出应类似于下面这样（包括引号）：
#Albert Einstein once said, “A person who never made a mistake never tried anything new.”
message1='说，"胸口碎大石，菊花开瓶盖。"'
print(name1.title()+message1)
#名言2： 重复练习2-5，但将名人的姓名存储在变量famous_person 中，再创建要显示的消息，并将其存储在变量message 中，然后打印这条消息。
#剔除人名中的空白： 存储一个人名，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合"\t" 和"\n" 各一次。
name2='\tbrother\nchun '
#打印这个人名，以显示其开头和末尾的空白。然后，分别使用剔除函数lstrip() 、rstrip() 和strip() 对人名进行处理，并将结果打印出来。
print(name2)
print(name2.rstrip())
print(name2.lstrip())
print(name2.strip())