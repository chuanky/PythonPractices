# define 定义，定义一个函数

def display_message():
    print("函数")

# summation 加法，相加
def sum(v1, v2):
    result = v1 + v2
    print(result)

# f(x) = ax + b
# 参数是x；return是f(x)
# fullName.title(), title()本身就是一个函数
# 这个函数没有输入，这个函数中的值是通过fullName中的值得到的
# 返回就相当于把fullName中的值，首字母大写
def get_formatted_name(firstName, lastName):
    fullName = firstName + ' ' + lastName
    return fullName

names = ['chuanqi','chunguang','haoke']
def printNames(names):
    name = names.pop()
    print(name)

printNames(names[:])
print(names)
printNames(names)
print(names)