# 8-6 城市名 ：编写一个名为city_country() 的函数，它接受城市的名称及其所属的国家。这个函数应返回一个格式类似于下面这样的字符串：
# "Santiago, Chile"
# 至少使用三个城市-国家对调用这个函数，并打印它返回的值。
def city_country(city,country):
    city_name = city.title()+' '+country.title()
    return city_name
beijing = city_country('beijing','china')
print(beijing)
tokyo = city_country('tokyo','japan')
print(tokyo)
shanghai = city_country('shanghai','china')
print(shanghai)

# 8-7 专辑 ：编写一个名为make_album() 的函数，它创建一个描述音乐专辑的字典。这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。使
# 用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。
def make_album(name,music):
    album_discribe = {'name':name.title(),'music':music.title()}
    return album_discribe
music1 = make_album('jay','yehuimei')
print(music1)
music2 = make_album('JJ','jiangnan')
print(music2)
music3 = make_album('chen li','yiranyibaozha')
print(music3)
# 给函数make_album() 添加一个可选形参，以便能够存储专辑包含的歌曲数。如果调用这个函数时指定了歌曲数，就将这个值添加到表示专辑的字典中。调用这个
# 函数，并至少在一次调用中指定专辑包含的歌曲数。
def make_album(name,music,number = 0):
    if number == 0:
        album_discribe = {'name':name.title(),'music':music.title()}
    else:
        album_discribe = {'name':name.title(),'music':music.title(),'song number':str(number)}
    return album_discribe
music4 = make_album('wang lihong','weiyi')
music5 = make_album('huazhou','chushan',6)
print(music4)
print(music5)

# 8-8 用户的专辑 ：在为完成练习8-7编写的程序中，编写一个while 循环，让用户输入一个专辑的歌手和名称。获取这些信息后，使用它们来调用函
# 数make_album() ，并将创建的字典打印出来。在这个while 循环中，务必要提供退出途径。
active=True
while active:
    print("Please tell me the singer's name ande the music name:")
    print("enter 'q' at any time to quit")
    name = input('singer name:')
    if name == 'q':
        break
    music = input('music name:')
    if music == 'q':
        break
    album = make_album(name,music)
    print(album)
