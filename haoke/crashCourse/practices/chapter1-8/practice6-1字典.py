#6-1 人 ：使用一个字典来存储一个熟人的信息，包括名、姓、年龄和居住的城市。该字典应包含键first_name 、last_name 、age 和city 。将存储在该字典中
#的每项信息都打印出来。
infor_chuanqi = {'first_name':'chuanqi','last_name':'shi','age':'28','city':'nanjing'}
print(infor_chuanqi['first_name'])
print(infor_chuanqi['last_name'])
print(infor_chuanqi['age'])
print(infor_chuanqi['city'])
#6-2 喜欢的数字 ：使用一个字典来存储一些人喜欢的数字。请想出5个人的名字，并将这些名字用作字典中的键；想出每个人喜欢的一个数字，并将这些数字作为值存
#储在字典中。打印每个人的名字和喜欢的数字。为让这个程序更有趣，通过询问朋友确保数据是真实的。
favourite_number = {'chuanqi':'2','chunguang':'3','paopao':'5','zhuxi':'7','lijie':'9'}
print("Chuanqi's favourite number is "+favourite_number['chuanqi']+'!')
print("Chunguang's favourite number is "+favourite_number['chunguang']+'!')
print("Paopao's favourite number is "+favourite_number['paopao']+'!')
print("Zhuxi's favourite number is "+favourite_number['zhuxi']+'!')
print("Lijie's favourite number is "+favourite_number['lijie']+'!')
#6-3 词汇表 ：Python字典可用于模拟现实生活中的字典，但为避免混淆，我们将后者称为词汇表。
#想出你在前面学过的5个编程词汇，将它们用作词汇表中的键，并将它们的含义作为值存储在词汇表中。
python_words = {'print':'输出','if':'条件函数','while':'循环','append':'列表添加'}
#以整洁的方式打印每个词汇及其含义。为此，你可以先打印词汇，在它后面加上一个冒号，再打印词汇的含义；也可在一行打印词汇，再使用换行符（\n ）插
#入一个空行，然后在下一行以缩进的方式打印词汇的含义。