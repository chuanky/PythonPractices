#6-4 词汇表2 ：既然你知道了如何遍历字典，现在请整理你为完成练习6-3而编写的代码，将其中的一系列print 语句替换为一个遍历字典中的键和值的循环。确定该
#循环正确无误后，再在词汇表中添加5个Python术语。当你再次运行这个程序时，这些新术语及其含义将自动包含在输出中。
python_words = {'print':'输出','if':'条件函数','while':'循环','append':'列表添加'}
for word,meaning in python_words.items():
    print('\n'+word.title()+'的意思是'+meaning+'。')
#6-5 河流 ：创建一个字典，在其中存储三条大河流及其流经的国家。其中一个键—值对可能是'nile': 'egypt' 。
Big_rivres = {'amazon river':'brazil','nile':'egypt','the Yangtse River':'china'}
for river,country in Big_rivres.items():
    print('\n'+river.title()+' runs through '+country.title()+'.')
#使用循环为每条河流打印一条消息，如“The Nile runs through Egypt.”。
for river in Big_rivres.keys():
    print('\n'+river.title())
#使用循环将该字典中每条河流的名字都打印出来。
for country in Big_rivres.values():
    print('\n'+country.title())
#使用循环将该字典包含的每个国家的名字都打印出来。
#6-6 调查 ：在6.3.1节编写的程序favorite_languages.py中执行以下操作。
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
#创建一个应该会接受调查的人员名单，其中有些人已包含在字典中，而其他人未包含在字典中。
name_list = ['jen','sarah','chuanqi','chunguang','xuyang']
#遍历这个人员名单，对于已参与调查的人，打印一条消息表示感谢。对于还未参与调查的人，打印一条消息邀请他参与调查。
for name in name_list:
    if name in favorite_languages.keys():
        print(name.title()+' 感谢你的参与！')
    else:
        print(name.title()+' 请填写调查问卷！')