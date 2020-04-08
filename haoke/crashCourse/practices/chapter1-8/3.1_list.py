#3-1 姓名： 将一些朋友的姓名存储在一个列表中，并将其命名为names 。依次访问该列表中的每个元素，从而将每个朋友的姓名都打印出来。
friends=['传奇','春哥','泡泡']
print(friends[0])
print(friends[1])
print(friends[2])
#3-2 问候语： 继续使用练习3-1中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
message='！我妈喊你过来吃饭！'
print(friends[0]+message)
print(friends[1]+message)
print(friends[2]+message)
#3-3 自己的列表： 想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含多种通勤方式的列表。根据该列表打印一系列有关这些通勤方式的宣言，如“I wouldlike to own a Honda motorcycle”。
names=['神州1号','神州2号','神州8号']
message1='我想开'
message2='去上学！'
print(message1+names[0]+message2)
print(message1+names[1]+message2)
print(message1+names[2]+message2)
