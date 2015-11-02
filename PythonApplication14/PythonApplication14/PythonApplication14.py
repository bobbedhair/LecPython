#coding: cp949
#Lec14-1102: XML, Json�Ľ�


##############################################XML �Ľ�

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



##lxml �ļ� ��ġ ��
#f=open('alcohol.xml', encoding='utf-8')
#xml=f.read()
#soup=BeautifulSoup(xml, 'lxml')
#for nodes in soup.alcohol('cate1'):
#    #if nodes['tt']=="����":       #���ǰ˻�
#    print('Cate1: '+nodes['tt'])
#    for node in nodes('cate2'):
#        print('\tCate2: '+node['tt'])
#        for item in node('item'):
#            print('\t\t'+item.string)



##############################################Json �Ľ�

import json

#data={1:'a', 2:'b'}
#data2=json.dumps(data)
#data3=json.loads(data2)
#print(type(data2))
#print(type(data3))

#data={1:'�츮', 2:'����'}
#data2=json.dumps(data, ensure_ascii=False)  #�⺻���� True, �ѱ� ����Ҷ� False�� ����
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

data=json.loads(s, object_hook=JsonObject)  #Ŭ���� ���� �Ӽ� �߰�

print(data.name)
print(data.detail)
print(data.detail.last)
for email in data.emails:
    print(email)
