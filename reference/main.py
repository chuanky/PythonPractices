l = [3, 2, 1] #列表，有序的
dic = {'key': ['value', 'value1'], 'key1': 'value1'} #字典，无序的

'''
    f(x, y) = x + y = return
    f -> function -> 某种功能
    sum(x, y) = x + y
'''

# 函数，function
def m_sum(x, y):
    result = x + y
    return result

print(m_sum(1, 3))

# 类，class
class Person():
    # initialization
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def grow(self):
        self.age += 1

class ShanghaiPerson(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def talk(self):
        return "说上海话"

s = ShanghaiPerson('moli', 18)
print(s.name + " " + s.talk())
p = Person('haoke', 20)
# p.talk()
    

# p = Person('haoke', 29)
# p1 = Person('moli', 18)


# '''列表其实是一个系统自带的类'''
# l = [3, 2, 1] 
# print(l)
# l.sort()
# l.append(4)
# l.append({'key':'value'})
# print(l)