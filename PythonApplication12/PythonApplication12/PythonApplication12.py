coding: cp949
Lec12-1026: ����ǥ����2

import re


str='''Window
Unix
Linux
Solaris'''

#����, �ٹٲ��� ������ ��� ����, 1�� �̻�
#��Ƽ���� �÷��� �� �����ϸ� Window�� ���
p=re.compile('^.+', re.M)   
print(p.findall(str))

p=re.compile('^.+', re.S)
print(p.search(str))



#Group�� �̸� �����ϱ�
m=re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
print(m.group('first_name', 'last_name'))
print(m.groups())

m=re.match(r"(\d+)\.?(\d+)?", "24")
print(m.groups())
print(m.groups(20))

m=re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
print(m.groupdict())



#Lookahead assertion
p=re.compile(".+:")
m=p.search("http://google.com")
print(m.group())

p=re.compile(".+(?=:)")
m=p.search("http://google.com")
print(m.group())



import os
import glob
os.chdir("C:\/")
print(os.getcwd())
print(glob.glob("*"))

p=re.compile('.*[.](?!bat$|exe$).*$')   #.bat�� .exe ���� ����



#Lookbehind assertion
p=re.compile("(?<=abc)def")
m=p.search("abcdef")
print(m.group())

m=re.search('(?<=-)\w+', 'spam-egg')
print(m.group())



#start(), end()
email="tony@tiremove_thisger.net"
m=re.search("remove_this", email)
result=email[:m.start()]+email[m.end():]
print(result)



#Ȩ������ html ���� ����
import urllib.request
with urllib.request.urlopen('http://www.naver.com') as f:
        print(f.read())
        print(f.read(300))  #300����Ʈ
        print(f.read(300).decode("utf-8"))