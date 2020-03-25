names = ['haoke', 'chunguang', 'chuanqi']
name_dict = {'name':'haoke','weight':'160'}

print(name_dict['name'])
print(name_dict['weight'])

#Java
# for (int i = 0; i < 10; i++){
#     System.out.println(i);
# }
#Python
# for i in range(0, 10):
#     print(i)

# 流程控制
# for
# while
# if
# elif
# else

# 基础变量类型
# int
# float
# str

# 数据类型
# list = [x, y, z]
# dictionary = {k1:v1, k2:v2, k3:v3}



for key, value in name_dict.items():
    print(key)
    print(value)
#pop 用处是剔除list中最后一个元素，返回最后一个元素
# responses = {}
# # 设置一个标志，指出调查是否继续
# polling_active = True
# while polling_active:
# # 提示输入被调查者的名字和回答
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")
# # 将答卷存储在字典中
#     responses[name] = response
# # 看看是否还有人要参与调查
#     repeat = input("Would you like to let another person respond? (yes/ no) ")
#     if repeat == 'no':
#         polling_active = False
# # 调查结束，显示结果
# print("\n--- Poll Results ---")
# for name, response in responses.items():
#     print(name + " would like to climb " + response + ".")

