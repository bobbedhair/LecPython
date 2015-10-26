coding: cp949
Lec12-1026: 정규표현식2

import re


str='''Window
Unix
Linux
Solaris'''

#시작, 줄바꿈을 제외한 모든 문자, 1개 이상
#멀티라인 플래그 값 제외하면 Window만 출력
p=re.compile('^.+', re.M)   
print(p.findall(str))

p=re.compile('^.+', re.S)
print(p.search(str))



#Group에 이름 지정하기
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

p=re.compile('.*[.](?!bat$|exe$).*$')   #.bat와 .exe 파일 제외



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



#홈페이지 html 문서 추출
import urllib.request
with urllib.request.urlopen('http://www.naver.com') as f:
        print(f.read())
        print(f.read(300))  #300바이트
        print(f.read(300).decode("utf-8"))