import json

curdir = 'reference/jsonExamples'
file_path = curdir + '/股票列表.txt'

def init_stock_list(file_path):
    '''读取装在txt文件中的股票json数据，返回股票字典：{code : stock_info}'''
    stocks_dict = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)
        stock_list = json_data['stockList']
        
        for stock in stock_list:
            cur = Stock(stock['orgId'],
                        stock['category'],
                        stock['code'],
                        stock['pinyin'],
                        stock['zwjc'])
            stocks_dict[stock['code']] = cur
    
    return stocks_dict


class Stock():
    '''封装一只股票的信息'''
    def __init__(self, orgId, category, code, pinyin, zwjc):
        self.orgId = orgId
        self.category = category
        self.code = code
        self.pinyin = pinyin
        self.zwjc = zwjc

    def toString(self):
        print("股票代码: " + self.code + ", 中文名称: " + self.zwjc)

stock_dict = init_stock_list(file_path)

while True:
    try:
        code = input("输入股票代码：")
        if code == 'quit':
            break
        stock = stock_dict[code]
    except:
        print("代码为：" + code + "的股票不存在")
    else:
        stock.toString()
