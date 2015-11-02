#coding: cp949
#Lec14-1102: XML, Json파싱


##############################################XML 파싱

#from bs4 import BeautifulSoup

#f = open('test.xml')
#xml = f.read()
#soup = BeautifulSoup(xml, "html.parser")
#for node in soup.findAll('node'):
#    print("Node : "+node.string)
#    print("Attr1 : "+node['attr1'])



#f = open('song.xml', encoding='utf-8')
#xml = f.read()
#soup = BeautifulSoup(xml, "html.parser")
#for nodes in soup.test('song'):
#    for node in nodes:
#       print(node.string)



##lxml 파서 설치 후
#f=open('alcohol.xml', encoding='utf-8')
#xml=f.read()
#soup=BeautifulSoup(xml, 'lxml')
#for nodes in soup.alcohol('cate1'):
#    #if nodes['tt']=="안주":       #조건검색
#    print('Cate1: '+nodes['tt'])
#    for node in nodes('cate2'):
#        print('\tCate2: '+node['tt'])
#        for item in node('item'):
#            print('\t\t'+item.string)



##############################################Json 파싱

import json

#data={1:'a', 2:'b'}
#data2=json.dumps(data)
#data3=json.loads(data2)
#print(type(data2))
#print(type(data3))

#data={1:'우리', 2:'나라'}
#data2=json.dumps(data, ensure_ascii=False)  #기본값은 True, 한글 사용할때 False로 설정
#print(data2)



s = """
{
"name": "cybaek",
"detail" : { "last": "baek" },
"emails": [ "cybaek@xxx.com", "cybaek@yyy.com" ]
}
"""

data=json.loads(s)

print(data['name'])
print(data['detail'])
print(data['detail']['last'])
print()


class JsonObject:
    def __init__(self, d):
        self.__dict__=d

data=json.loads(s, object_hook=JsonObject)  #클래스 사용시 속성 추가

print(data.name)
print(data.detail)
print(data.detail.last)
for email in data.emails:
    print(email)
