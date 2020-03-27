#6-7 人 ：在为完成练习6-1而编写的程序中，再创建两个表示人的字典，然后将这三个字典都存储在一个名为people 的列表中。遍历这个列表，将其中每个人的所有
#信息都打印出来。
infor_chuanqi = {'first_name':'chuanqi','last_name':'shi','age':'28','city':'nanjing'}
infor_chunguang = {'first_name':'chunguang','last_name':'li','age':'29','city':'shenzhen'}
infor_paopao = {'first_name':'jiaqi','last_name':'li','age':'28','city':'beijing'}
people = [infor_chuanqi,infor_chunguang,infor_paopao]
for infor in people:
    print(infor)
#6-8 宠物 ：创建多个字典，对于每个字典，都使用一个宠物的名称来给它命名；在每个字典中，包含宠物的类型及其主人的名字。将这些字典存储在一个名为pets
#的列表中，再遍历该列表，并将宠物的所有信息都打印出来。
infor_xiaohuang = {'name':'xiaohuang','species':'dog','owner':'chuanqi'}
infor_xiaopang = {'name':'xiaopang','species':'pig','owner':'chuguang'}
infor_xiaoguai = {'name':'xiaoguai','species':'cat','owner':'haoke'}
pets = [infor_xiaohuang,infor_xiaopang,infor_xiaoguai]
for pet in pets:
    print('\n'+'宠物名字：'+pet['name'].title())
    print('宠物种类：'+pet['species'])
    print('宠物主人：'+pet['owner'].title())

#6-9 喜欢的地方 ：创建一个名为favorite_places 的字典。在这个字典中，将三个人的名字用作键；对于其中的每个人，都存储他喜欢的1~3个地方。为让这个练
#习更有趣些，可让一些朋友指出他们喜欢的几个地方。遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。
favorite_places = {'chuanqi':['北京','上海','杭州'],'chuguang':['深圳','成都'],'haoke':['天津','重庆']}
for name,places in favorite_places.items():
    print('\n'+name.title()+"'s favaourite places are:")
    for city in places:
        print('\t'+city)
#6-10 喜欢的数字 ：修改为完成练习6-2而编写的程序，让每个人都可以有多个喜欢的数字，然后将每个人的名字及其喜欢的数字打印出来。
favourite_number = {'chuanqi':[2,3,4],'chunguang':[4,5,6],'paopao':[7,9],'zhuxi':[1,5],'lijie':[50,100]}
for name,numbers in favourite_number.items():
    print('\n'+name.title()+"'s favourite numbers are:")
    for number in numbers:
        print('\t'+str(number))

#6-11 城市 ：创建一个名为cities 的字典，其中将三个城市名用作键；对于每座城市，都创建一个字典，并在其中包含该城市所属的国家、人口约数以及一个有关该
#城市的事实。在表示每座城市的字典中，应包含country 、population 和fact 等键。将每座城市的名字以及有关它们的信息都打印出来。
cities = {
    'beijing':{
        'country':'china',
        'population':'50,000,000',
        'fact':'有故宫'
        },

    'tokyo':{
        'country':'japan',
        'population':'20,000,000',
        'fact':'有寿司'},

    'paris':{
        'country':'France',
        'population':'15,000,000',
        'fact':'有铁塔'}
    }
for city,infor in cities.items():
    print(city.title()+'是'+infor['country']+'的首都，有'+infor['population']+'人口，有趣的是那里'+infor['fact']+'。')
#6-12 扩展 ：本章的示例足够复杂，可以以很多方式进行扩展了。请对本章的一个示例进行扩展：添加键和值、调整程序要解决的问题或改进输出的格式。 
