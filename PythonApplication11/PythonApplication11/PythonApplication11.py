#coding: cp949
#Lec11-1014: ����ǥ����1

import re

#pattern=re.compile("d")

#result=pattern.search("dog")
#print(result)

#result2=pattern.search("dog", 1)
#print(result2)



#��Ƽ���� ��� �ɼ�
#str='''sample1.
#sample2.
#sample3.'''
##p=re.compile("^.*", re.S)   #���� �������
#p=re.compile(".*$")   #������ ����
#result=p.search(str)
#print(result.group())



#group ����ϱ�
#str=" abc 1234 xyz "
#pattern=re.compile("\s*[a-zA-Z]+\s+(\d+)+\s+([a-zA-Z]+)\s*")
#result=pattern.match(str)
#print(result.group(1))
#print(result.group(2))



#fullmatch ����ϱ�
#pattern=re.compile("o[gh]")
#result1=pattern.fullmatch("dog")
#result2=pattern.fullmatch("ogre")
#result3=pattern.fullmatch("doggie", 1, 3)   #0���� 2����
#print(result1)
#print(result2)
#print(result3)



#split ����ϱ�
#pattern=re.compile("\W+")
#result=pattern.split("words, words, words.")
#result2=pattern.split("words, words, words.", 1)
#print(result)
#print(result2)

#pattern = re.compile("x*")
#result = pattern.split('axbc')
#print(result)



#Ž������ ��Ī
#str= '<a href="index.html">HERE</a><font size="10">'
#result = re.search(r'href="(.*?)">', str)   #�����Ǵ� ���� �� �̻�X
#print(result.group(1))



#�ֹε�Ϲ�ȣ ���Խ� ����
id="940323-2019123"
pattern=re.compile("\d{6}-\d{7}")
result=pattern.fullmatch(id)
print(result)
#print(result.group(1))
#print(result.group(2))