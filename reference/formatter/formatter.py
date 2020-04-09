text = ''

while True:
    if text == 'quit':
        break
    text = input("输入想要转换的字符: ")
    print(text.lower().title())


